# Frequently Asked Questions (FAQ)

## General Questions

### Q: What is MLX?
**A**: MLX is Apple's machine learning framework optimized for Apple Silicon. It provides native acceleration through the Metal GPU and Neural Engine, offering better performance and efficiency than PyTorch on Mac.

### Q: Do I need an Apple Silicon Mac to use these models?
**A**: Yes, these models are specifically optimized for M1/M2/M3/M4 chips. They won't work on Intel Macs or other platforms.

### Q: Can I use these models commercially?
**A**: Yes, but please check the original model licenses:
- PaddleOCR-VL: Apache 2.0
- Hunyuan-MT: Check Tencent's license

---

## Installation & Setup

### Q: How do I install MLX?
**A**: 
```bash
pip install mlx mlx-lm
```

### Q: What Python version do I need?
**A**: Python 3.9 or higher is required.

### Q: Do I need to install CUDA or PyTorch?
**A**: No! MLX models run natively without PyTorch or CUDA dependencies.

### Q: I'm getting "ImportError: No module named 'mlx'"
**A**: Make sure you're using the correct Python environment:
```bash
which python3
pip3 install mlx mlx-lm
```

---

## Model Usage

### Q: How much RAM do I need?
**A**: 
- PaddleOCR-VL: Minimum 8GB, recommended 16GB+
- Hunyuan-MT-Q8: Minimum 16GB, recommended 32GB+

### Q: Can I run both models simultaneously?
**A**: Yes, but you'll need at least 32GB RAM for comfortable performance.

### Q: How do I download the models?
**A**: Models are automatically downloaded from Hugging Face when you first use them:
```python
from mlx_lm import load
model, tokenizer = load("biabia-55/Hunyuan-MT-Chimera-7B-MLX-Q8")
```

### Q: Where are models stored?
**A**: By default in `~/.cache/huggingface/hub/`

---

## Performance

### Q: Why is the first inference slow?
**A**: The first run includes model loading and Metal shader compilation. Subsequent runs are much faster.

### Q: How can I improve performance?
**A**: 
1. Close other applications to free up RAM
2. Use smaller batch sizes
3. Ensure your Mac is plugged in (not on battery)
4. Update to the latest macOS version

### Q: Is MLX faster than PyTorch on Mac?
**A**: Yes, typically 1.5-2.5x faster for these models. See [performance_benchmarks.md](performance_benchmarks.md).

---

## OCR (PaddleOCR-VL)

### Q: What image formats are supported?
**A**: JPG, PNG, TIFF, and most common formats supported by PIL.

### Q: What's the maximum image size?
**A**: Recommended maximum is 2048x2048. Larger images will be resized.

### Q: Can it handle scanned PDFs?
**A**: Yes, but you need to convert PDF pages to images first. See examples.

### Q: Does it preserve formatting?
**A**: Yes, the model attempts to preserve layout, tables, and formatting in the output.

### Q: What languages are supported?
**A**: Chinese, English, and mixed Chinese-English text. Other languages may work but aren't officially supported.

---

## Translation (Hunyuan-MT)

### Q: How many languages are supported?
**A**: 200+ languages. See the model card for the full list.

### Q: Can I translate long documents?
**A**: Yes, but split them into chunks of ~500 tokens for best results.

### Q: How accurate is the translation?
**A**: The 8-bit quantized version has ~2% quality loss compared to the original FP16 model. See benchmarks.

### Q: Can I fine-tune the model?
**A**: Not currently supported in this release. Contact us if you need this feature.

---

## Troubleshooting

### Q: "RuntimeError: Metal device not found"
**A**: This means you're not on an Apple Silicon Mac. These models only work on M1/M2/M3/M4.

### Q: Model download is very slow
**A**: 
1. Check your internet connection
2. Try using a VPN if Hugging Face is slow in your region
3. Download manually and specify local path

### Q: "Out of memory" error
**A**: 
1. Close other applications
2. Reduce batch size
3. Use a smaller model variant
4. Upgrade your RAM

### Q: Results are different from PyTorch
**A**: Minor numerical differences are expected due to quantization and different computation backends. Quality should be similar overall.

### Q: Can I run this on Google Colab?
**A**: No, Colab doesn't have Apple Silicon. Use Hugging Face Spaces or run locally on Mac.

---

## Development

### Q: Can I contribute to this project?
**A**: Yes! See CONTRIBUTING.md for guidelines.

### Q: How do I report a bug?
**A**: Open an issue on GitHub with:
- Your Mac model and RAM
- macOS version
- MLX version
- Error message and stack trace

### Q: Can you convert model X to MLX?
**A**: Maybe! Open an issue with your request and we'll consider it.

### Q: Where's the conversion code?
**A**: See the `conversion/` directories in each model folder.

---

## Licensing & Attribution

### Q: Do I need to credit you when using these models?
**A**: Not required, but appreciated! Please credit the original model authors.

### Q: Can I use this in my app?
**A**: Yes, but check the original model licenses for any restrictions.

### Q: Can I redistribute these models?
**A**: The models are on Hugging Face under their respective licenses. Link to the HF repos rather than redistributing.

---

## Getting Help

### Q: Where can I get more help?
**A**: 
1. Check the documentation in `docs/`
2. Search existing GitHub issues
3. Open a new issue with details
4. Join the discussion on Hugging Face

### Q: Is there a Discord/Slack?
**A**: Not yet, but we're considering it based on community interest.

---

## Future Plans

### Q: Will you support 4-bit quantization?
**A**: It's on the roadmap! Follow the repo for updates.

### Q: What about other models?
**A**: We're considering:
- More vision-language models
- Smaller/faster variants
- Other popular models

Vote on GitHub issues to help prioritize!

---

*Last updated: 2025-12-26*

**Didn't find your question?** Open an issue on GitHub!
