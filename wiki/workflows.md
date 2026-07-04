# 常用工作流

## 交接文档驱动任务

模式：

1. 用户提供 `交接_Codex_*.md` 文档。
2. Codex 读取文档和项目目录。
3. Codex 按文档执行任务。
4. Codex 运行校验。
5. Codex 汇报产物路径、统计和异常。

来源：`raw/conversations/2026-06-22-initial-context.md`

## LLM Wiki 知识库更新

模式：

1. 新事实先写入 `raw/`。
2. 更新 `wiki/` 中受影响页面。
3. 更新 `wiki/provenance.md`。
4. 运行 `python scripts/audit_kb.py`。
5. `git add .`
6. `git commit`
7. `git push`

来源：`raw/sources/2026-06-22-karpathy-llm-wiki.md`

## 通过 skill 操作个人知识库

用户希望把个人知识库维护流程封装成通用 skill。当前可用的 skill 是 `$personal-llm-wiki`，支持记录、查询、编译 wiki、审计、提交和推送。

本地路径：

```text
C:\Users\Administrator\.codex\skills\personal-llm-wiki
```

来源：`raw/sources/2026-06-22-personal-llm-wiki-skill.md`

## 在其他 agent 中安装 personal-llm-wiki

推荐方式：

1. 在目标机器或目标 agent 可访问的位置 clone 仓库：

```powershell
git clone git@github.com:turen1/knowledge.git D:\knowledge
```

2. 将仓库内置 skill 复制或链接到该 agent 的 skills 目录：

```powershell
Copy-Item -Recurse D:\knowledge\skills\personal-llm-wiki $env:USERPROFILE\.codex\skills\
```

3. 之后使用 `$personal-llm-wiki`。

如果 agent 支持显式加载 skill 路径，也可以直接使用：

```text
D:\knowledge\skills\personal-llm-wiki\SKILL.md
```

`kb.py` 会自动从 skill 所在目录向上查找 `.git`、`raw/`、`wiki/`，因此 clone 到哪里，哪里就是本地知识库根目录。

来源：`raw/sources/2026-06-22-embed-skill-in-knowledge-repo.md`

## 复杂任务先提问再执行

复杂任务不要直接进入生成或编码，先让 AI 扮演导师逐步提问，澄清目标、边界、约束、验收标准和潜在盲点。回答模糊时继续追问，确认完整理解后再执行。

适用场景：

- 产品设计、商业分析、UI/UX 和系统架构。
- Cocos Creator 复杂功能，例如背包系统、技能 Buff 状态机、存档系统、物理碰撞、对象池和渲染性能优化。
- 多 agent 协作前的需求澄清：先由导师 agent 明确问题，再分派执行 agent。

来源：`raw/sources/2026-06-26-jikoujiang-ask-before-execute-prompt-video-analysis.md`

## 游戏开发多模型协作

游戏开发中，多模型协作应按角色分工，而不是让多个模型同时写同一批代码：

- Claude：负责设计规范、系统边界、数据契约、复杂架构审查和疑难问题分析。
- Codex：负责实现、跨文件重构、测试、构建、浏览器/GUI 验证、Git 工作流和交付。
- Gemini：负责多模态分析、高吞吐批处理、截图/录屏/音频/PDF 分析，以及 Google 技术栈相关任务。

关键原则：同一功能、同一分支、同一组文件应保持单一写入者，其他模型只做设计、审查或分析。

来源：`raw/sources/2026-06-26-ai-coding-models-game-development-comparison.md`

## 专业分镜表构建

专业分镜表不是画面清单，而是把导演意图、摄影执行、剪辑节奏、美术调度、声音设计和制作成本压缩成可执行蓝图。核心判断标准是：导演、摄影、剪辑、演员、美术、制片拿到后，都能知道这一镜为什么拍、怎么拍、拍多久、需要什么、和前后镜头如何衔接。

推荐流程：

1. 先读剧本并提取戏剧任务、视角主导者、基调和节奏。
2. 建立视觉总谱：空间平面图、表演区、摄影机禁区、180 度轴线、主光方向、色彩定调和剪辑节奏。
3. 拆解镜头序列：每镜明确镜号、画面草图、景别、机位/角度、镜头运动、画面内容、人物调度、台词/旁白、音效/音乐、时长、转场、道具/服化/美术和备注。
4. 注入动态关系：用箭头、多格画面、起幅/落幅、焦点转移、动作匹配、图形匹配、视线顺接和声音先入，让静态画格具备时间和剪辑逻辑。
5. 添加施工注释：为摄影、美术、录音、演员、特效、制片分别标注执行要点、风险、设备、成本和备选方案。
6. 修改时保留可追溯性：新增镜头用 `12A`、`12B` 等尾号，不重排全片镜号；现场修改保留原始痕迹。

关键原则：

- 每个镜头必须有功能；删掉后不会少信息或情绪的镜头应删改或合并。
- 先设计观众应感到什么，再决定景别、机位、运动和剪辑点。
- 景别、角度、运动、声音和时长都要服务信息释放与心理节奏。
- 分镜阶段就要考虑建立镜头、反应镜头、细节特写、动作衔接、视线衔接、声音衔接、安全镜头和转场镜头。
- 好分镜需要同时满足看得懂、拍得出、剪得顺、有情绪、控成本。

来源：`raw/sources/2026-07-04-storyboard-construction-ideas.md`、`raw/sources/2026-07-04-storyboard-construction-process.md`、`raw/sources/2026-07-04-storyboard-table-rules.md`
