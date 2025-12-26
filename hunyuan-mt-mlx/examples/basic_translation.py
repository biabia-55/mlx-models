#!/usr/bin/env python3
"""
Basic Translation Example using Hunyuan-MT-Chimera-7B-MLX-Q8

This example demonstrates how to use the Hunyuan-MT model
for multilingual translation on Apple Silicon.
"""

from mlx_lm import load, generate
import sys

def translate(model, tokenizer, text, src_lang="English", tgt_lang="Chinese"):
    """
    Translate text from source language to target language.
    
    Args:
        model: Loaded MLX model
        tokenizer: Loaded tokenizer
        text: Text to translate
        src_lang: Source language name
        tgt_lang: Target language name
    
    Returns:
        Translated text
    """
    prompt = f"Translate the following {src_lang} text to {tgt_lang}:\n{text}\n\nTranslation:"
    
    result = generate(
        model,
        tokenizer,
        prompt=prompt,
        max_tokens=512,
        temp=0.3,  # Lower temperature for more accurate translation
        verbose=False
    )
    
    return result

def main():
    print("🚀 Loading Hunyuan-MT-Chimera-7B-MLX-Q8...")
    
    # Load model
    model_id = "biabia-55/Hunyuan-MT-Chimera-7B-MLX-Q8"
    model, tokenizer = load(model_id)
    
    print("✅ Model loaded successfully!")
    print()
    
    # Example translations
    examples = [
        {
            "text": "Artificial intelligence is transforming the world.",
            "src": "English",
            "tgt": "Chinese"
        },
        {
            "text": "机器学习是人工智能的一个重要分支。",
            "src": "Chinese",
            "tgt": "English"
        },
        {
            "text": "Hello, how are you today?",
            "src": "English",
            "tgt": "French"
        }
    ]
    
    # If text provided as argument, translate it
    if len(sys.argv) >= 2:
        text = " ".join(sys.argv[1:])
        src_lang = input("Source language (default: English): ").strip() or "English"
        tgt_lang = input("Target language (default: Chinese): ").strip() or "Chinese"
        
        print(f"\n🔄 Translating from {src_lang} to {tgt_lang}...")
        print(f"📝 Original: {text}")
        
        result = translate(model, tokenizer, text, src_lang, tgt_lang)
        
        print(f"✨ Translation: {result}")
    else:
        # Run examples
        print("📚 Running example translations...\n")
        
        for i, example in enumerate(examples, 1):
            print(f"Example {i}:")
            print(f"  Source ({example['src']}): {example['text']}")
            
            result = translate(
                model, 
                tokenizer, 
                example['text'],
                example['src'],
                example['tgt']
            )
            
            print(f"  Target ({example['tgt']}): {result}")
            print()

if __name__ == "__main__":
    main()
