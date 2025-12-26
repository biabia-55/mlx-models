# PaddleOCR-VL MLX Web UI

🌐 **Beautiful web interface for PaddleOCR-VL-MLX**

A modern, user-friendly web application for optical character recognition powered by PaddleOCR-VL-MLX.

## ✨ Features

- 📸 **Drag & Drop Upload** - Easy image and PDF upload
- 🔄 **Real-time OCR** - Instant text recognition
- 📄 **Multi-format Support** - Images (JPG, PNG) and PDFs
- 💾 **Export Options** - Download results as TXT, DOCX, or PDF
- 📊 **History Tracking** - View and manage past OCR tasks
- 🎨 **Modern UI** - Clean, responsive design
- ⚡ **Fast Processing** - Optimized for Apple Silicon

## 🚀 Quick Start

### Prerequisites

- macOS with Apple Silicon (M1/M2/M3/M4)
- Python 3.9+
- PaddleOCR-VL-MLX model (automatically downloaded)

### Installation

```bash
# Clone the repository
git clone https://github.com/biabia-55/mlx-models.git
cd mlx-models/paddleocr-vl-mlx/web-ui

# Install dependencies
pip install flask pillow python-docx reportlab pymupdf

# Install PaddleOCR-VL-MLX
pip install transformers
```

### Running the App

#### Option 1: Using the launch script (Recommended)

```bash
chmod +x start_ocr_ui.sh
./start_ocr_ui.sh
```

The browser will automatically open to `http://localhost:5001`

#### Option 2: Manual start

```bash
python3 app_mlx_ocr.py
```

Then open your browser to `http://localhost:5001`

## 📖 Usage

### 1. Upload an Image or PDF

- Click the upload area or drag & drop your file
- Supported formats: JPG, PNG, PDF

### 2. Start OCR

- Click "开始识别" (Start Recognition)
- Wait for processing (usually 2-3 seconds per image)

### 3. View Results

- See the recognized text in real-time
- Edit if needed

### 4. Export

Choose your preferred format:
- **TXT**: Plain text file
- **DOCX**: Microsoft Word document
- **PDF**: Formatted PDF with preserved layout

## 🎨 Screenshots

### Main Interface
![Main UI](screenshots/main-ui.png)

### OCR Results
![Results](screenshots/results.png)

### History View
![History](screenshots/history.png)

## 🔧 Configuration

Edit `app_mlx_ocr.py` to customize:

```python
# Server settings
PORT = 5001
HOST = '0.0.0.0'  # Change to '127.0.0.1' for local-only access

# Upload folder
UPLOAD_FOLDER = '/tmp/mlx_ocr_uploads'

# Output folder
OUTPUT_FOLDER = './outputs'
```

## 📊 Performance

Tested on M4 Max (128GB):

| File Type | Size | Processing Time |
|-----------|------|-----------------|
| Single Image (1MB) | 1920x1080 | ~2.5s |
| PDF (10 pages) | 5MB | ~25s |
| Scanned Document | 2MB | ~3s |

## 🐛 Troubleshooting

### Port already in use

```bash
# Kill existing process
lsof -ti:5001 | xargs kill -9

# Or change port in app_mlx_ocr.py
```

### Model not loading

```bash
# Verify model installation
python3 -c "from transformers import AutoTokenizer; AutoTokenizer.from_pretrained('gamhtoi/PaddleOCR-VL-MLX', trust_remote_code=True)"
```

### PDF processing fails

```bash
# Install PyMuPDF
pip install pymupdf
```

## 🔒 Security Notes

- This is designed for **local use only**
- Don't expose to the internet without proper authentication
- Uploaded files are stored temporarily in `/tmp`
- Clear history regularly for privacy

## 🛠️ Development

### Project Structure

```
web-ui/
├── app_mlx_ocr.py          # Flask application
├── start_ocr_ui.sh         # Launch script
├── templates/              # HTML templates
│   └── index.html
├── static/                 # CSS, JS, images
│   ├── css/
│   ├── js/
│   └── img/
└── README.md              # This file
```

### Adding Features

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 API Endpoints

### POST /ocr

Upload and process an image/PDF

**Request:**
```json
{
  "file": "<multipart/form-data>"
}
```

**Response:**
```json
{
  "task_id": "uuid",
  "status": "processing"
}
```

### GET /status/<task_id>

Check OCR task status

**Response:**
```json
{
  "status": "completed",
  "result": "recognized text...",
  "confidence": 0.95
}
```

### GET /history

Get OCR history

**Response:**
```json
{
  "history": [
    {
      "timestamp": "2024-12-26 18:00:00",
      "filename": "document.pdf",
      "result": "..."
    }
  ]
}
```

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](../../CONTRIBUTING.md)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../../LICENSE) file for details.

## 🙏 Acknowledgments

- [PaddleOCR-VL](https://huggingface.co/PaddlePaddle/PaddleOCR-VL) - Original model
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [MLX](https://github.com/ml-explore/mlx) - Apple Silicon acceleration

## 📮 Contact

- GitHub: [@biabia-55](https://github.com/biabia-55)
- Hugging Face: [@gamhtoi](https://huggingface.co/gamhtoi)

---

**Made with ❤️ for the Apple Silicon community**
