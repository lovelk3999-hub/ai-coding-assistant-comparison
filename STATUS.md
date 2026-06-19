# 状态 STATUS — AI代码生成工具对比

> 最后更新：2026-06-19
> 当前阶段：Phase 1 数据采集中

---

## 总体进度

| 模块 | 状态 | 备注 |
|------|------|------|
| 方向选定 | ✅ 已完成 | 第6轮实地调研确认 |
| 数据采集 | 🚧 进行中 | 01已完成，02进行中 |
| tools.json | ⏳ 待启动 | 数据结构参考 ai-video-tools-comparison |
| 模板编写 | ⏳ 待启动 | 改 base.html/tool.html/compare.html |
| generate.py | ⏳ 待启动 | 改数据源和模板路径 |
| 本地生成 | ⏳ 待启动 | python scripts/generate.py |
| GitHub仓库 | ⏳ 待启动 | 新建仓库 |
| Cloudflare部署 | ⏳ 待启动 | 配置Pages |
| GA4 + Search Console | ⏳ 待启动 | 配置分析工具 |

---

## 已完成任务

- [x] **01-调研市场名单** — 列出15个AI coding assistant工具，含官网URL、分类、定位
  - 产出: done/01-tools-list.md

---

## 进行中

- [ ] **02-采集各工具官网定价** — 当前执行

---

## 待办清单

- [ ] 02-采集各工具官网定价数据
- [ ] 03-采集功能特性数据
- [ ] 04-采集第三方评分数据
- [ ] 05-编写 data/tools.json
- [ ] 06-修改 templates/ 模板文件
- [ ] 07-修改 scripts/generate.py + 本地生成
- [ ] 08-创建 GitHub 仓库 + 配置 Cloudflare Pages
- [ ] 09-配置 GA4 + Search Console
- [ ] 10-申请 Google AdSense

---

## 技术参考

- **参考项目**: E:\ai\program\google seo web\ai-video-tools-comparison\
- **生成脚本**: scripts/generate.py
- **数据结构**: data/tools.json
- **模板**: templates/base.html, index.html, tool.html, compare.html
- **部署**: Cloudflare Pages + GitHub main 分支

---

## 已知问题

1. Windows GBK 终端编码 → 文件读写必须 encoding="utf-8"
2. PowerShell 不支持 && → 用 ; 或分多次执行
3. 数据采集可能遇反爬 → 参考 ai-video-tools-comparison 的 Playwright 方案
