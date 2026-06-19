# 06. 修改 templates/ 模板文件

## 任务描述
复制 ai-video-tools-comparison 的模板，修改为AI代码生成工具对比的样式。

## 详细步骤

### Step 1: 复制参考模板
从 E:\ai\program\google seo web\ai-video-tools-comparison\templates\
复制4个文件：base.html / index.html / tool.html / compare.html

### Step 2: 修改
- base.html：网站名称/品牌色/GA4占位符
- index.html：标题改为"AI代码生成工具对比"
- tool.html：对比维度字段匹配features{}结构
- compare.html：调整对比表头

### Step 3: 添加FAQ结构化数据
在base.html中添加FAQ JSON-LD

## 预期产出
- templates/base.html, index.html, tool.html, compare.html

## 完成标准
- [ ] 4个模板文件全部修改完成
- [ ] 匹配AI代码生成工具对比的对比维度
- [ ] 已更新 STATUS.md
- [ ] 本文件已移入 done/
## Checkpoint 规则（重要！）

执行过程中，每完成一步就更新 doing/CHECKPOINT.md：

```markdown
# CHECKPOINT - {时间}
## 当前任务
06-修改 templates/ 模板文件
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