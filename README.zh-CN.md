# 竞赛答辩 PPT：整页模板优先 Skill

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-111827)](SKILL.md)
[![Workflow](https://img.shields.io/badge/Workflow-template--first-0f766e)](references/workflow.md)
[![License](https://img.shields.io/badge/License-MIT-f59e0b)](LICENSE)
[![skills.sh](https://skills.sh/b/che626/competition-ppt-template-first-skill)](https://skills.sh/che626/competition-ppt-template-first-skill)

> 先把页面当作完整的视觉作品设计出来，再把关键内容做成可编辑 PPT。

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

## 快速安装与使用

将仓库放进支持 `SKILL.md` 的 Agent Skills 目录，或使用兼容的安装器：

```bash
npx -y skills@latest add che626/competition-ppt-template-first-skill \
  --skill competition-ppt-template-first \
  --agent codex \
  --global
```

然后在对话中附上作品报告、真实截图和参考页，直接这样使用：

```text
$competition-ppt-template-first
读取作品报告和素材图，为 AI 视觉应用竞赛做一份 11 页答辩 PPT。
先输出事实登记表、PPT 目录、每页放什么和需要哪些真实图片；
再生成一张高完成度的代表页模板图，确认风格后再批量制作。
```

更多可直接复制的提示词见 [examples/prompt-recipes.md](examples/prompt-recipes.md)。

发布前可运行下面的检查，确认 `skills` CLI 能真实识别该仓库，而不是只在 GitHub 页面上“看起来没问题”：

```powershell
.\scripts\validate-distribution.ps1
```

发布到 GitHub 后可追加 `-Remote`，再验证远端克隆与发现流程。

## 项目工作目录

```text
competition-ppt/
  00_plan/       事实登记表、叙事主线、逐页蓝图
  01_templates/  已确认的整页模板图与提示词记录
  02_build/      可编辑 PPTX 制作文件
  03_renders/    PPT 导出预览与检查记录
  04_approved/   用户明确满意的页面
  99_retired/    被淘汰的方案，保留用于追溯
```

详细规范见 [references/project-conventions.md](references/project-conventions.md)。

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
- [`templates/deck-brief.md`](templates/deck-brief.md)：整套 PPT 的设计总控表
- [`templates/revision-record.md`](templates/revision-record.md)：将用户反馈转成结构性修改的记录

## 安装

克隆仓库，或将整个文件夹放到 Codex 的 skills 目录；入口文件是 `SKILL.md`。

仓库不包含真实项目截图、获奖证书或其他私密素材，只包含通用方法和匿名示例。

## 适用与边界

- 最适合创新创业、AI、机器人、工程、科研、产品原型类竞赛答辩。
- 不伪造数据、获奖、系统能力或企业落地情况。
- 不要求所有视觉元素都拆成形状：背景模板可以是一张高完成度图片，但真实截图、数据、标题和正文必须可替换、可编辑。
- 每套完整 PPT 必须先做一张代表页，用户确认后再批量制作，避免整套成品走偏。

欢迎提交通用、已获得发布权的版式经验与规范。贡献前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。
