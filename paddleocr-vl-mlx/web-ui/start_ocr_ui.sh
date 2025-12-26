#!/bin/bash
# PaddleOCR-VL MLX UI Launcher

# 切换到项目目录
cd "/Users/gt/NLLB_Translation"

# 检查 Flask 是否已在运行
if lsof -Pi :5001 -sTCP:LISTEN -t >/dev/null ; then
    echo "Server already running on port 5001."
else
    echo "Starting OCR Server..."
    /opt/homebrew/bin/python3 app_mlx_ocr.py > /tmp/mlx_ocr_server.log 2>&1 &
    sleep 3
fi

# 打开浏览器
open "http://localhost:5001"

echo "✨ OCR UI 启动成功！"
