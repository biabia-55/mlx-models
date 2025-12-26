from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import sys
import uuid
import json
import threading
from datetime import datetime
from pathlib import Path
from PIL import Image
import docx
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# 核心路径配置
BASE_DIR = '/Users/gt/NLLB_Translation'
sys.path.append(BASE_DIR)
sys.path.append('/Users/gt/.gemini/antigravity/scratch/paddleocr-mlx-conversion')

try:
    from paddleocr_mlx import PaddleOCRMLX
    ocr_client = PaddleOCRMLX()
except Exception as e:
    print(f"❌ 初始化模型失败: {e}")
    ocr_client = None

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

app = Flask(__name__)
UPLOAD_FOLDER = '/tmp/mlx_ocr_uploads'
HISTORY_FILE = os.path.join(BASE_DIR, 'ocr_history.json')
OUTPUT_FOLDER = os.path.join(BASE_DIR, 'outputs')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# 任务状态存储
tasks_status = {}

def save_history(entry):
    history = []
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                history = json.load(f)
        except:
            pass
    history.insert(0, entry)
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history[:100], f, ensure_ascii=False, indent=2)

def get_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def generate_files(task_id, content, original_name):
    base_name = os.path.splitext(original_name)[0]
    ts = datetime.now().strftime("%H%M%S")
    
    # MD
    md_path = os.path.join(OUTPUT_FOLDER, f"{base_name}_{ts}.md")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # Word
    docx_path = os.path.join(OUTPUT_FOLDER, f"{base_name}_{ts}.docx")
    doc = docx.Document()
    for line in content.split('\n'):
        doc.add_paragraph(line)
    doc.save(docx_path)
    
    # PDF 升级版：解决偷工减料问题
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    
    pdf_path = os.path.join(OUTPUT_FOLDER, f"{base_name}_{ts}.pdf")
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # 定义中文字体样式
    try:
        font_path = "/System/Library/Fonts/Supplemental/Songti.ttc"
        pdfmetrics.registerFont(TTFont('Song', font_path))
        chinese_style = ParagraphStyle(
            'ChineseStyle',
            fontName='Song',
            fontSize=10,
            leading=14,
            wordWrap='CJK'  # 开启中日韩换行支持
        )
    except:
        chinese_style = styles["Normal"]

    elements = []
    for line in content.split('\n'):
        if not line.strip():
            elements.append(Spacer(1, 12))
            continue
        # 使用 Paragraph 实现自动换行，彻底杜绝 [:100] 截断
        p = Paragraph(line, chinese_style)
        elements.append(p)
        elements.append(Spacer(1, 6))
        
    doc.build(elements)
    
    return {
        'md': os.path.basename(md_path),
        'docx': os.path.basename(docx_path),
        'pdf': os.path.basename(pdf_path)
    }

def process_heavy_task(task_id, filepath, original_name, mode, layout_mode=False):
    ext = os.path.splitext(original_name)[1].lower()
    full_text = []
    
    # 初始化 result 字段
    tasks_status[task_id]['result'] = ""
    
    try:
        if ext == '.pdf':
            doc = fitz.open(filepath)
            total_pages = len(doc)
            for i in range(total_pages):
                # 使用 update 增量更新进度，保留 result 字段内容
                tasks_status[task_id].update({
                    'status': 'processing', 
                    'progress': int((i/total_pages)*100), 
                    'page': i+1, 
                    'total': total_pages
                })
                
                page = doc.load_page(i)
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
                tmp_img = f"{filepath}_p{i}.png"
                pix.save(tmp_img)
                
                # 开启真正的 token 流式推理
                current_page_text = ""
                for token in ocr_client.predict(tmp_img, prompt=mode, layout_mode=layout_mode, stream=True):
                    current_page_text += token
                    # 实时组合出当前已有的全部内容
                    prefix = "\n\n".join(full_text)
                    tasks_status[task_id]['result'] = (prefix + "\n\n" + current_page_text) if prefix else current_page_text
                
                full_text.append(current_page_text)
                os.remove(tmp_img)
        else:
            tasks_status[task_id].update({'status': 'processing', 'progress': 50})
            current_text = ""
            for token in ocr_client.predict(filepath, prompt=mode, layout_mode=layout_mode, stream=True):
                current_text += token
                tasks_status[task_id]['result'] = current_text
            full_text.append(current_text)
            
        final_content = "\n\n".join(full_text)
        files = generate_files(task_id, final_content, original_name)
        
        entry = {
            'id': task_id,
            'name': original_name,
            'time': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'files': files,
            'summary': final_content[:150] + "..."
        }
        save_history(entry)
        tasks_status[task_id].update({'status': 'completed', 'result': final_content, 'files': files})
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        tasks_status[task_id].update({'status': 'error', 'message': str(e)})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/history')
def history():
    return jsonify(get_history())

@app.route('/status/<task_id>')
def status(task_id):
    return jsonify(tasks_status.get(task_id, {'status': 'not_found'}))

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

@app.route('/predict', methods=['POST'])
def predict():
    if not ocr_client: return jsonify({'error': '模型未加载'}), 500
    file = request.files.get('file')
    if not file: return jsonify({'error': '没有文件'}), 400
    
    mode = request.form.get('mode', 'OCR:')
    task_id = str(uuid.uuid4())
    ext = os.path.splitext(file.filename)[1].lower()
    filepath = os.path.join(UPLOAD_FOLDER, f"{task_id}{ext}")
    file.save(filepath)
    
    # 检查是否开启了排版模式
    layout_mode = request.form.get('layout_mode') == 'true'
    
    tasks_status[task_id] = {'status': 'pending', 'progress': 0, 'result': ''}
    
    # 异步处理
    thread = threading.Thread(target=process_heavy_task, args=(task_id, filepath, file.filename, mode, layout_mode))
    thread.start()
    
    return jsonify({'task_id': task_id})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)
