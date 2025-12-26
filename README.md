# MLX Models for Apple Silicon

🚀 **Production-ready MLX implementations of popular AI models, optimized for Apple Silicon (M1/M2/M3/M4)**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![MLX](https://img.shields.io/badge/MLX-0.4+-green.svg)](https://github.com/ml-explore/mlx)

## 🌟 Available Models

### 1. PaddleOCR-VL-MLX
**World's first MLX-native OCR model**

- 🔗 [Model on Hugging Face](https://huggingface.co/biabia-55/PaddleOCR-VL-MLX)
- 📦 Size: ~2GB
- ⚡ Speed: 2-3s per image on M4 Max
- 🎯 Use case: Document digitization, receipt processing, academic paper OCR

### 2. Hunyuan-MT-Chimera-7B-MLX-Q8
**8-bit quantized multilingual translation model**

- 🔗 [Model on Hugging Face](https://huggingface.co/biabia-55/Hunyuan-MT-Chimera-7B-MLX-Q8)
- 📦 Size: 4.2GB (70% smaller than original)
- ⚡ Speed: 25 tokens/s on M4 Max
- 🌍 Languages: 200+
- 🎯 Use case: Document translation, real-time translation, multilingual chat

## 🚀 Quick Start

### Installation

```bash
# Install MLX and dependencies
pip install mlx mlx-lm transformers pillow

# Clone this repo for examples
git clone https://github.com/biabia-55/mlx-models.git
cd mlx-models
```

### OCR Example

```python
from transformers import AutoTokenizer
from PIL import Image

# Load model
tokenizer = AutoTokenizer.from_pretrained(
    "biabia-55/PaddleOCR-VL-MLX",
    trust_remote_code=True
)

# Process image
image = Image.open("document.jpg")
# See paddleocr-vl-mlx/examples/ for complete code
```

### Translation Example

```python
from mlx_lm import load, generate

# Load model
model, tokenizer = load("biabia-55/Hunyuan-MT-Chimera-7B-MLX-Q8")

# Translate
prompt = "Translate to French: Hello, world!"
result = generate(model, tokenizer, prompt=prompt, max_tokens=256)
print(result)
```

## 📊 Performance Benchmarks

Tested on M4 Max (128GB RAM):

| Model | Task | Speed | Memory | vs PyTorch |
|-------|------|-------|--------|------------|
| PaddleOCR-VL-MLX | OCR | 2-3s/image | ~4GB | 2.5x faster |
| Hunyuan-MT-MLX-Q8 | Translation | 25 tok/s | ~8GB | 1.67x faster |

## 📁 Repository Structure

```
mlx-models/
├── paddleocr-vl-mlx/          # PaddleOCR-VL examples and tools
│   ├── examples/              # Usage examples
│   ├── conversion/            # PyTorch → MLX conversion scripts
│   └── README.md
├── hunyuan-mt-mlx/            # Hunyuan-MT examples and tools
│   ├── examples/              # Usage examples
│   ├── quantization/          # Quantization scripts
│   └── README.md
├── docs/                      # Documentation
│   ├── performance_benchmarks.md
│   ├── conversion_guide.md
│   └── faq.md
└── README.md                  # This file
```

## 🎯 Use Cases

### Document Processing Pipeline
```python
# See paddleocr-vl-mlx/examples/document_pipeline.py
from paddleocr_mlx import OCRPipeline

pipeline = OCRPipeline()
result = pipeline.process("document.pdf")
# Preserves formatting, tables, and layout
```

### Real-time Translation
```python
# See hunyuan-mt-mlx/examples/streaming_translation.py
from hunyuan_mlx import StreamingTranslator

translator = StreamingTranslator()
for chunk in translator.translate_stream("Long text..."):
    print(chunk, end='', flush=True)
```

### Batch Processing
```python
# See examples for batch processing multiple files
# Optimized for throughput on Apple Silicon
```

## 🛠️ Development

### Converting Your Own Models

See [docs/conversion_guide.md](docs/conversion_guide.md) for detailed instructions on converting PyTorch models to MLX.

### Running Tests

```bash
python -m pytest tests/
```

## 📚 Documentation

- [Performance Benchmarks](docs/performance_benchmarks.md)
- [Conversion Guide](docs/conversion_guide.md)
- [FAQ](docs/faq.md)
- [API Reference](docs/api_reference.md)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [PaddlePaddle Team](https://github.com/PaddlePaddle/PaddleOCR) for PaddleOCR-VL
- [Tencent Hunyuan Team](https://huggingface.co/Tencent-Hunyuan) for Hunyuan-MT
- [Apple ML Research](https://github.com/ml-explore/mlx) for the MLX framework
- [Hugging Face](https://huggingface.co) for model hosting

## 📮 Contact

- GitHub: [@biabia-55](https://github.com/biabia-55)
- Hugging Face: [@biabia-55](https://huggingface.co/biabia-55)
- Email: wheiwalee@gmail.com

## ⭐ Star History

If you find this project useful, please consider giving it a star!

---

**Made with ❤️ for the Apple Silicon community**
