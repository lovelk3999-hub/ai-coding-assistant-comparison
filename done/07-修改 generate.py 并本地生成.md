# 07. 修改 generate.py 并本地生成

## 任务描述
复制参考项目的 generate.py，修改后本地运行生成所有页面。

## 详细步骤

### Step 1: 复制
复制 ai-video-tools-comparison/scripts/generate.py 到 scripts/

### Step 2: 修改
- DATA_FILE / TEMPLATE_DIR / OUTPUT_DIR 路径
- SITE_NAME / SITE_URL 品牌配置
- 按需调整生成逻辑

### Step 3: 运行
python scripts/generate.py

### Step 4: 检查
- output/index.html 存在
- 每个工具有独立页面
- 对比页正确生成
- sitemap.xml + robots.txt 存在
- OG标签 / canonical / meta desc 都有

## 预期产出
- scripts/generate.py（修改版）
- output/ 所有静态页面

## 完成标准
- [ ] 生成成功无报错
- [ ] 所有页面正常
- [ ] 已更新 STATUS.md
- [ ] 本文件已移入 done/
## Checkpoint 规则（重要！）

执行过程中，每完成一步就更新 doing/CHECKPOINT.md：

```markdown
# CHECKPOINT - {时间}
## 当前任务
07-修改 generate.py 并本地生成
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