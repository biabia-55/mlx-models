#!/bin/bash
# GitHub Repository Setup Script

echo "🚀 Setting up MLX Models GitHub Repository"
echo ""

# Navigate to the repo directory
cd /Users/gt/NLLB_Translation/mlx-models-github

# Initialize git if not already done
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
    git branch -M main
else
    echo "✅ Git repository already initialized"
fi

# Create .gitignore
echo "📝 Creating .gitignore..."
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
ENV/
env/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Model files (stored on Hugging Face)
*.safetensors
*.bin
*.gguf
*.npz

# Logs
*.log

# Jupyter
.ipynb_checkpoints/
*.ipynb

# Testing
.pytest_cache/
.coverage
htmlcov/

# Temporary files
tmp/
temp/
*.tmp
EOF

# Add all files
echo "➕ Adding files to git..."
git add .

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: MLX models for Apple Silicon

- PaddleOCR-VL-MLX examples and documentation
- Hunyuan-MT-MLX-Q8 examples and documentation
- Performance benchmarks
- FAQ and guides
"

echo ""
echo "✅ Repository setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Create a new repository on GitHub: https://github.com/new"
echo "2. Repository name: mlx-models"
echo "3. Description: Production-ready MLX implementations for Apple Silicon"
echo "4. Make it public"
echo "5. Don't initialize with README (we already have one)"
echo ""
echo "Then run these commands:"
echo "  git remote add origin https://github.com/gamhtoi/mlx-models.git"
echo "  git push -u origin main"
echo ""
echo "🎉 Happy coding!"
