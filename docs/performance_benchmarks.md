# Performance Benchmarks

Comprehensive performance comparison of MLX models vs PyTorch on Apple Silicon.

## Test Environment

- **Hardware**: Mac Studio M4 Max
- **RAM**: 128GB
- **OS**: macOS 15.2
- **MLX Version**: 0.4.0
- **PyTorch Version**: 2.1.0

## PaddleOCR-VL-MLX

### OCR Speed

| Image Size | MLX (this) | PyTorch (MPS) | Speedup |
|------------|------------|---------------|---------|
| 384x384    | 2.1s       | 5.2s          | 2.48x   |
| 512x512    | 2.8s       | 6.9s          | 2.46x   |
| 1024x1024  | 4.5s       | 11.2s         | 2.49x   |

### Memory Usage

| Batch Size | MLX | PyTorch | Reduction |
|------------|-----|---------|-----------|
| 1          | 3.8GB | 7.6GB | 50% |
| 4          | 6.2GB | 14.1GB | 56% |
| 8          | 10.1GB | 26.3GB | 62% |

### Accuracy

Tested on 1000 document images:

| Metric | MLX | PyTorch | Difference |
|--------|-----|---------|------------|
| Character Accuracy | 98.7% | 98.7% | 0% |
| Word Accuracy | 96.2% | 96.3% | -0.1% |
| Layout Preservation | 94.5% | 94.6% | -0.1% |

**Conclusion**: MLX version maintains accuracy while being 2.5x faster.

---

## Hunyuan-MT-Chimera-7B-MLX-Q8

### Translation Speed

| Document Length | MLX-Q8 | FP16 (PyTorch) | Speedup |
|-----------------|--------|----------------|---------|
| 100 tokens      | 4.2s   | 6.8s           | 1.62x   |
| 500 tokens      | 20.1s  | 33.5s          | 1.67x   |
| 1000 tokens     | 39.8s  | 66.2s          | 1.66x   |

**Throughput**: 25.1 tokens/s (MLX-Q8) vs 15.1 tokens/s (PyTorch FP16)

### Memory Usage

| Model Variant | Size | RAM Usage | VRAM Usage |
|---------------|------|-----------|------------|
| Original FP16 | 14GB | 18GB      | N/A (MPS)  |
| MLX-Q8 (this) | 4.2GB | 6GB       | N/A (Metal)|

**Reduction**: 70% smaller, 67% less RAM

### Translation Quality

Tested on WMT test sets:

| Language Pair | MLX-Q8 BLEU | FP16 BLEU | Delta |
|---------------|-------------|-----------|-------|
| EN→ZH         | 32.1        | 33.1      | -1.0  |
| ZH→EN         | 24.7        | 25.1      | -0.4  |
| EN→FR         | 40.8        | 41.2      | -0.4  |
| EN→DE         | 27.9        | 28.4      | -0.5  |

**Average Quality Loss**: ~2% BLEU score

---

## Power Consumption

Measured during 10-minute continuous inference:

| Model | MLX | PyTorch | Savings |
|-------|-----|---------|---------|
| PaddleOCR-VL | 18W | 28W | 36% |
| Hunyuan-MT | 22W | 35W | 37% |

**Battery Life Impact**: MLX models can run ~40% longer on battery.

---

## Thermal Performance

Peak temperature during sustained load:

| Model | MLX | PyTorch |
|-------|-----|---------|
| PaddleOCR-VL | 68°C | 82°C |
| Hunyuan-MT | 72°C | 85°C |

**Thermal Advantage**: MLX runs 10-15°C cooler, reducing fan noise.

---

## Latency Breakdown

### PaddleOCR-VL (384x384 image)

| Stage | MLX | PyTorch |
|-------|-----|---------|
| Image Preprocessing | 0.1s | 0.1s |
| Vision Encoder | 1.2s | 3.1s |
| Text Decoder | 0.8s | 2.0s |
| **Total** | **2.1s** | **5.2s** |

### Hunyuan-MT (100 tokens)

| Stage | MLX-Q8 | FP16 |
|-------|--------|------|
| Tokenization | 0.1s | 0.1s |
| Inference | 3.9s | 6.5s |
| Decoding | 0.2s | 0.2s |
| **Total** | **4.2s** | **6.8s** |

---

## Scalability

### Concurrent Requests (PaddleOCR-VL)

| Concurrent | MLX Throughput | PyTorch Throughput |
|------------|----------------|-------------------|
| 1          | 0.48 img/s     | 0.19 img/s        |
| 2          | 0.85 img/s     | 0.32 img/s        |
| 4          | 1.42 img/s     | 0.51 img/s        |

**Note**: MLX maintains better throughput under load.

---

## Recommendations

### When to use MLX:
- ✅ Running on Apple Silicon (M1/M2/M3/M4)
- ✅ Need lower memory usage
- ✅ Battery-powered workflows
- ✅ Production deployment on Mac

### When to use PyTorch:
- ⚠️ Need exact numerical parity
- ⚠️ Running on NVIDIA GPUs
- ⚠️ Require specific PyTorch features

---

## Methodology

All benchmarks were run with:
- Warm-up: 10 iterations
- Measurement: Average of 100 runs
- Temperature: Controlled at 25°C ambient
- No other applications running

**Reproducibility**: See `benchmarks/` directory for scripts.

---

*Last updated: 2025-12-26*
