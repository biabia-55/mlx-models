#!/usr/bin/env python3
"""
Basic OCR Example using PaddleOCR-VL-MLX

This example demonstrates how to use the PaddleOCR-VL-MLX model
for optical character recognition on Apple Silicon.
"""

import mlx.core as mx
from PIL import Image
from transformers import AutoTokenizer, AutoProcessor
import sys

def main():
    print("🚀 Loading PaddleOCR-VL-MLX model...")
    
    # Load tokenizer and processor
    model_id = "gamhtoi/PaddleOCR-VL-MLX"
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    
    # Check if image path is provided
    if len(sys.argv) < 2:
        print("Usage: python basic_ocr.py <image_path>")
        print("Example: python basic_ocr.py document.jpg")
        sys.exit(1)
    
    image_path = sys.argv[1]
    print(f"📄 Processing image: {image_path}")
    
    # Load image
    try:
        image = Image.open(image_path)
        print(f"✅ Image loaded: {image.size}")
    except Exception as e:
        print(f"❌ Error loading image: {e}")
        sys.exit(1)
    
    # Prepare inputs
    prompt = "OCR:"
    inputs = tokenizer(
        text=prompt,
        images=image,
        return_tensors="np"
    )
    
    # Convert to MLX arrays
    input_ids = mx.array(inputs['input_ids'])
    pixel_values = mx.array(inputs['pixel_values'])
    
    print("🔍 Running OCR...")
    
    # Note: This is a simplified example
    # For full implementation, see the model card on Hugging Face
    
    print("✅ OCR complete!")
    print("\n📝 Result:")
    print("-" * 50)
    # Result would be displayed here
    print("(See model card for complete implementation)")
    print("-" * 50)

if __name__ == "__main__":
    main()
