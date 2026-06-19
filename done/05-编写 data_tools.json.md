# 05. 编写 data/tools.json

## 任务描述
将任务01-04采集的所有数据，按标准格式整理为 data/tools.json。

## 详细步骤

### Step 1: 参考格式
打开 ai-video-tools-comparison/data/tools.json 看完整格式。

### Step 2: 编写
每条工具数据的字段：
```json
{
  "id": "tool-name",
  "name": "工具名",
  "description": "一句话描述",
  "category": "分类",
  "url": "https://...",
  "plans": [...],
  "features": {...},
  "g2_rating": 4.5,
  "g2_reviews": 100,
  "reddit_posts": [...]
}
```

### Step 3: Checkpoint
每写完5个工具，更新 doing/CHECKPOINT.md

### Step 4: 验证
用 python -c 验证JSON格式正确

## 预期产出
- data/tools.json（15个工具的完整数据）

## 完成标准
- [ ] 15个工具数据完整
- [ ] JSON格式正确
- [ ] 已更新 STATUS.md
- [ ] 本文件已移入 done/
## Checkpoint 规则（重要！）

执行过程中，每完成一步就更新 doing/CHECKPOINT.md：

```markdown
# CHECKPOINT - {时间}
## 当前任务
05-编写 data/tools.json
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

> **省token提示**: **强烈建议用Agnes做这个任务**！把原始数据丢给 agnesChat，让Agnes格式化输出JSON。
> 调用方式：require('./agnes_helper').formatToolsJson(rawData)