# 08. 创建GitHub仓库+Cloudflare部署

## 任务描述
创建GitHub仓库，配置Cloudflare Pages自动部署。

## 详细步骤

### Step 1: GitHub仓库
打开 github.com/new，仓库名建议 ai-AI-coding-assistant-comparison
设为 Public，不初始化

### Step 2: 推送代码
git init; git add .; git commit -m 'init'
git remote add origin [仓库URL]
git push -u origin main

### Step 3: Cloudflare Pages
dash.cloudflare.com -> Pages -> Create -> Connect Git
选择仓库 -> 框架None -> 输出目录 output

### Step 4: 验证
访问 *.pages.dev 域名确认部署成功

## 预期产出
- GitHub 仓库已创建并推送
- Cloudflare Pages 已配置并部署

## 完成标准
- [ ] GitHub仓库已创建
- [ ] Cloudflare部署成功
- [ ] 页面可访问
- [ ] 已更新 STATUS.md
- [ ] 本文件已移入 done/
## Checkpoint 规则（重要！）

执行过程中，每完成一步就更新 doing/CHECKPOINT.md：

```markdown
# CHECKPOINT - {时间}
## 当前任务
08-创建GitHub仓库+Cloudflare部署
## 已完成
- 子步骤1 -> 完成
- 子步骤2 -> 完成
## 下一步
- 下一步操作
## 已产出中间文件
- 位置
```

> 每完成一个子步骤就checkpoint，context压缩时不丢进度。
> 任务全部完成后删除 CHECKPOINT.md，本任务移入 done/。

> **省token提示**: 部署相关的Git操作，用 Shell 直接执行，不需要Agnes。