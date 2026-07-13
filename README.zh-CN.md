# 竞赛答辩 PPT：整页模板优先 Skill

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-111827)](skills/competition-ppt-template-first/SKILL.md)
[![Workflow](https://img.shields.io/badge/Workflow-template--first-0f766e)](skills/competition-ppt-template-first/references/workflow.md)
[![License](https://img.shields.io/badge/License-MIT-f59e0b)](LICENSE)
[![skills.sh](https://skills.sh/b/che626/competition-ppt-template-first-skill)](https://skills.sh/che626/competition-ppt-template-first-skill)

> 先理清这套 PPT 要让谁相信什么、每页该出现什么，再把关键内容做成可编辑 PPT。

[English README](README.md)

## 它解决什么问题

常规的 AI 做 PPT 往往是“深色背景 + 一堆边框 + 小字 + 相同卡片”。页面虽然完整，但没有主体、没有场景、没有层次，也不适合竞赛答辩。

本 Skill 推荐先完成下面的基础链路：先把文档和用户要求拆成清晰的叙事与视觉任务，逐页分析内容与布局，再按该页布局生成对应的整页背景模板图，最后填入可编辑内容，而不是直接套深色背景和几个框。

1. 先整理报告、附件、截图、数据中能用的内容和待补材料，判断这是答辩、产品展示、技术汇报还是研究说明。
2. 先写清楚受众、要达成的判断、叙事路线，以及项目本身可以成为画面的产品、场景、材质、设备、人物、样本或证据。
3. 为每页写清楚：本页结论与内容分组、阅读顺序、背景图是什么、主图是什么、有什么辅助视觉物件、真实图片放哪里、文字放哪里、哪些内容必须可编辑、这一页禁止出现什么。
4. 所有内容页都必须在布局确定后，生成或设计一张专属的整页背景模板图；技术信息密集页也要生成安静、留白明确的模板图，不得改回纯底色加原生卡片。封面和结尾页使用独立的主视觉模板。
5. 模板确认后，将其作为底层背景，再放入真实证据图片、可编辑文字和少量可替换覆盖层。
6. 导出重点页面检查文字、图片和层级，按反馈修改并归档满意版本。

## 两种使用深度

| 方式 | 适合情况 | 主要动作 |
| --- | --- | --- |
| `基础流程` | 只有赛题、简介、少量截图或已有 PPT。 | 分析结果目标、叙事类型和视觉元素；为每页写模板契约，再制作可编辑 PPT 并检查可读性。 |
| `文档溯源流程` | 有作品报告、论文、数据表、获奖证明或较完整技术资料。 | 在基础流程上补充来源清单、内容分析、事实登记、页级证据对应和逐页模板契约。 |

两种方式的视觉方法相同。文档溯源流程主要用于有数据、模型对比、奖项、技术指标等需要经得起追问的页面，不要求为了走流程而给每句普通叙述都建立复杂表格。两种方式都不能因为题目里有 AI，就默认每页都做成黑色、深蓝、青色发光的赛博风。

## 新能力：作品文档投喂到答辩路线

现在不需要先把文档手工总结一遍再让 AI 做 PPT。将作品报告、比赛要求、数据表、系统截图和奖项材料一并提供给 Skill，它会先完成：

```text
作品文档与素材
  -> 来源清单
  -> 内容分析：PPT 类型、受众、叙事、视觉元素、缺失项
  -> 可用事实与重点结论的来源对应
  -> 面向评委的答辩叙事路线
  -> 每页模板契约
  -> 代表页模板图
  -> 可编辑答辩 PPT
```

对于数据、模型对比、获奖、技术指标等关键结论，建议绑定事实编号与文档定位，例如“报告 S-01，第 4.2 节”或“数据表 S-03，Metrics 工作表 B8:F12”。资料未定的内容要保留为可替换区域或明确标注为未来计划，不要为了排版补造事实。完整做法见 [content-to-template-analysis.md](skills/competition-ppt-template-first/references/content-to-template-analysis.md)。

完整流程见 [source-ingestion.md](skills/competition-ppt-template-first/references/source-ingestion.md)，可以用下面命令初始化工作目录：

```text
python .\skills\competition-ppt-template-first\scripts\init-report-grounded-deck.py .\my-competition-deck --source-folder .\project-materials
```

## 关键方法

- 生图负责：构图、氛围、场景、材质、光影、整体高级感。
- PPT 负责：标题、正文、真实系统截图、数据、证书、图表和后续可替换内容。
- 内容越密集，背景越要暗、静、留白；内容越少，背景越可以丰富、有场景。
- 同一份 PPT 要统一标题位置、字级、色彩逻辑和材质气质，但不能每页都套同一种布局。
- 底层模板明显不对时，优先重新设计底层结构，不要靠在旧页面上不断叠新框修补。

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
先输出内容分析、PPT 叙事路线，并逐页写清背景场景、主视觉、真实图片位置、文字位置、辅助视觉物件和禁用元素；
再生成一张代表页模板图，确认风格后，对每一张内容页均先完成布局蓝图、再生成专属整页背景模板图、最后填入真实素材和可编辑文字。
```

更多可直接复制的提示词见 [prompt-recipes.md](skills/competition-ppt-template-first/examples/prompt-recipes.md)。

发布前可运行下面的检查，确认 `skills` CLI 能真实识别该仓库，而不是只在 GitHub 页面上“看起来没问题”：

```powershell
.\skills\competition-ppt-template-first\scripts\validate-distribution.ps1
```

发布到 GitHub 后可追加 `-Remote`，再验证远端克隆与发现流程。

## 项目工作目录

```text
competition-ppt/
  00_intake/     来源清单、提取笔记、原始素材引用
  00_plan/       内容分析、事实登记表、叙事主线、页级事实映射、逐页蓝图
  01_templates/  已确认的整页模板图与提示词记录
  02_build/      可编辑 PPTX 制作文件
  03_renders/    PPT 导出预览与检查记录
  04_approved/   用户明确满意的页面
  99_retired/    被淘汰的方案，保留用于追溯
```

详细规范见 [project-conventions.md](skills/competition-ppt-template-first/references/project-conventions.md)。

## 适用场景

- 创新创业、人工智能、机器人、工程、科研类竞赛答辩
- 项目路演、技术作品展示、产品原型展示
- 需要真实截图和技术证据支撑的高要求 PPT

## 核心文件

- [`SKILL.md`](skills/competition-ppt-template-first/SKILL.md)：给 AI 执行的完整流程
- [`workflow.md`](skills/competition-ppt-template-first/references/workflow.md)：从材料到成品的详细方法
- [`content-to-template-analysis.md`](skills/competition-ppt-template-first/references/content-to-template-analysis.md)：把文档、用户目标、产品/场景/素材拆成叙事路线和逐页模板要求
- [`layout-archetypes.md`](skills/competition-ppt-template-first/references/layout-archetypes.md)：痛点、方案、模型、迭代、系统、奖项、规划等页面结构
- [`source-ingestion.md`](skills/competition-ppt-template-first/references/source-ingestion.md)：读取作品文档、提取事实、建立答辩路线的方法
- [`quality-gates.md`](skills/competition-ppt-template-first/references/quality-gates.md)：导出后的质检清单
- [`slide-blueprint.md`](skills/competition-ppt-template-first/templates/slide-blueprint.md)：逐页设计蓝图
- [`fact-registry.md`](skills/competition-ppt-template-first/templates/fact-registry.md)：事实与证据登记表
- [`deck-brief.md`](skills/competition-ppt-template-first/templates/deck-brief.md)：整套 PPT 的设计总控表
- [`content-analysis.md`](skills/competition-ppt-template-first/templates/content-analysis.md)：PPT 类型、受众决策、视觉元素、风格依据、问题与假设的分析表
- [`source-manifest.md`](skills/competition-ppt-template-first/templates/source-manifest.md)：文档、要求、数据和素材的来源清单
- [`slide-source-map.md`](skills/competition-ppt-template-first/templates/slide-source-map.md)：每页结论与文档事实、真实证据的对应表
- [`revision-record.md`](skills/competition-ppt-template-first/templates/revision-record.md)：将用户反馈转成结构性修改的记录

## 安装

克隆仓库，或将 `skills/competition-ppt-template-first/` 放到 Codex 的 skills 目录；入口文件是该目录内的 `SKILL.md`。

仓库不包含真实项目截图、获奖证书或其他私密素材，只包含通用方法和匿名示例。

## 适用与边界

- 最适合创新创业、AI、机器人、工程、科研、产品原型类竞赛答辩，也可用于普通课程展示或项目汇报。
- 不伪造数据、获奖、系统能力或企业落地情况。
- 不要求所有视觉元素都拆成形状：背景模板可以是一张高完成度图片，但真实截图、数据、标题和正文必须可替换、可编辑。
- 制作整套 PPT 时，建议先做一张代表页确认视觉方向；已有成熟参考风格时可直接进入制作。
- 不把“AI”当成默认黑蓝赛博风的理由。背景、色彩、光影、产品/材质/场景要由项目本身和页面任务决定。

欢迎提交通用、已获得发布权的版式经验与规范。贡献前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。
