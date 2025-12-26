# 🔐 GitHub 推送指南

## 问题：需要认证

Git 推送需要身份验证。有两种方法：

---

## 方法 1: 使用 Personal Access Token（推荐，最简单）

### 步骤 1: 创建 Token

1. 访问：https://github.com/settings/tokens/new
2. 填写：
   - Note: `MLX Models Upload`
   - Expiration: `90 days` 或 `No expiration`
   - 勾选权限：
     - ✅ `repo` (全部勾选)
3. 点击 "Generate token"
4. **复制 Token**（只显示一次！）

### 步骤 2: 推送代码

在终端运行：

```bash
cd /Users/gt/NLLB_Translation/mlx-models-github

# 使用 HTTPS 方式（会提示输入密码）
git remote remove origin
git remote add origin https://github.com/biabia-55/mlx-models.git
git push -u origin main
```

当提示输入密码时：
- **Username**: `biabia-55`
- **Password**: 粘贴刚才复制的 Token（不是 GitHub 密码！）

---

## 方法 2: 使用 GitHub CLI（自动化）

### 安装 GitHub CLI

```bash
brew install gh
```

### 登录并推送

```bash
cd /Users/gt/NLLB_Translation/mlx-models-github

# 登录 GitHub
gh auth login
# 选择：GitHub.com → HTTPS → Yes → Login with a web browser

# 推送代码
git remote remove origin
git remote add origin https://github.com/biabia-55/mlx-models.git
git push -u origin main
```

---

## 方法 3: 设置 SSH 密钥（一劳永逸）

### 步骤 1: 生成 SSH 密钥

```bash
ssh-keygen -t ed25519 -C "wheiwalee@gmail.com"
# 按 Enter 使用默认路径
# 按 Enter 跳过密码（或设置密码）
```

### 步骤 2: 复制公钥

```bash
cat ~/.ssh/id_ed25519.pub
# 复制输出的内容
```

### 步骤 3: 添加到 GitHub

1. 访问：https://github.com/settings/ssh/new
2. Title: `Mac M4 Max`
3. Key: 粘贴刚才复制的公钥
4. 点击 "Add SSH key"

### 步骤 4: 推送代码

```bash
cd /Users/gt/NLLB_Translation/mlx-models-github
git remote remove origin
git remote add origin git@github.com:biabia-55/mlx-models.git
git push -u origin main
```

---

## 🎯 推荐方案

**如果您是第一次用 Git**：
→ 使用 **方法 1**（Personal Access Token）

**如果您经常用 Git**：
→ 使用 **方法 3**（SSH 密钥）

**如果您想最简单**：
→ 使用 **方法 2**（GitHub CLI）

---

## ✅ 验证推送成功

推送成功后，访问：
```
https://github.com/biabia-55/mlx-models
```

您应该看到：
- ✅ README 正确显示
- ✅ 所有文件都在
- ✅ 提交历史正常

---

**选择一个方法，然后告诉我结果！** 🚀
