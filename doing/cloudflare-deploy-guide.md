# Cloudflare Pages 部署指南

> 生成日期：2026-06-19
> GitHub仓库：https://github.com/lovelk3999-hub/ai-coding-assistant-comparison

## 快速部署步骤

1. **登录 Cloudflare Dashboard**
   - 打开 https://dash.cloudflare.com/
   - 登录你的Cloudflare账号

2. **创建 Pages 项目**
   - 左侧菜单 → Workers & Pages → Pages
   - 点击 "Create" → "Connect to Git"
   - 选择 GitHub 仓库：`lovelk3999-hub/ai-coding-assistant-comparison`
   - 授权 Cloudflare 访问你的 GitHub

3. **配置构建设置**
   - Project name: `ai-coding-tools`（或其他）
   - Production branch: `main`
   - Framework: None
   - Build command: 留空
   - Build output: `output`
   - Root directory: 留空

4. **部署**
   - 点击 "Save and Deploy"
   - 等待部署完成（约1-2分钟）
   - 自动获得 `*.pages.dev` 域名

5. **自定义域名（可选）**
   - 在 Pages 项目 → Custom domains → Set up a custom domain
   - 使用你自己的域名（需要先添加DNS）

6. **Cloudflare API Token（可选，用于后续自动化）**
   - 如希望 wrangler CLI 自动化部署，运行：`wrangler login`
   - 或在环境变量设置 `CLOUDFLARE_API_TOKEN`

## 项目配置备忘
- 输出目录：`output/`
- GitHub Actions 自动部署：Cloudflare Pages 自动监听 main 分支
- CDN：Cloudflare 全球CDN自动启用
- SSL：自动HTTPS
