# 竞赛答辩 PPT：整页模板优先 Skill

这是一个用于制作高完成度竞赛答辩 PPT 的 Codex Skill。它不是教你给 PPT 叠几个卡片，而是把一套经过反复修改验证的工作流固定下来：先分析材料和叙事，再生成整页视觉模板，最后拆成可编辑 PPT。

[English README](README.md)

## 它解决什么问题

常规的 AI 做 PPT 往往是“深色背景 + 一堆边框 + 小字 + 相同卡片”。页面虽然完整，但没有主体、没有场景、没有层次，也不适合竞赛答辩。

本 Skill 要求先完成下面的链路：

1. 从报告、附件、截图、数据中提取可验证事实。
2. 先写清楚每页要让评委相信什么、要放什么证据、需要哪些真实图片。
3. 按页面需求生成一张高完成度 16:9 模板图。
4. 模板确认后，将其拆成背景、真实证据图片、可编辑文字和少量可替换覆盖层。
5. 导出 PPT 实图检查，逐页根据反馈修改并归档满意版本。

## 关键方法

- 生图负责：构图、氛围、场景、材质、光影、整体高级感。
- PPT 负责：标题、正文、真实系统截图、数据、证书、图表和后续可替换内容。
- 内容越密集，背景越要暗、静、留白；内容越少，背景越可以丰富、有场景。
- 同一份 PPT 要统一标题位置、字级、色彩逻辑和材质气质，但不能每页都套同一种布局。
- 底层模板不对时，必须重新生成底层模板，不能靠在旧页面上不断叠新框修补。

## 适用场景

- 创新创业、人工智能、机器人、工程、科研类竞赛答辩
- 项目路演、技术作品展示、产品原型展示
- 需要真实截图和技术证据支撑的高要求 PPT

## 核心文件

- [`SKILL.md`](SKILL.md)：给 AI 执行的完整流程
- [`references/workflow.md`](references/workflow.md)：从材料到成品的详细方法
- [`references/layout-archetypes.md`](references/layout-archetypes.md)：痛点、方案、模型、迭代、系统、奖项、规划等页面结构
- [`references/quality-gates.md`](references/quality-gates.md)：导出后的质检清单
- [`templates/slide-blueprint.md`](templates/slide-blueprint.md)：逐页设计蓝图
- [`templates/fact-registry.md`](templates/fact-registry.md)：事实与证据登记表

## 安装

克隆仓库，或将整个文件夹放到 Codex 的 skills 目录；入口文件是 `SKILL.md`。

仓库不包含真实项目截图、获奖证书或其他私密素材，只包含通用方法和匿名示例。

