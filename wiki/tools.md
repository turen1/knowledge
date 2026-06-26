# 工具与环境

## 已知工具

- Codex
- Codex skill：`personal-llm-wiki`，路径 `C:\Users\Administrator\.codex\skills\personal-llm-wiki`，用于记录、更新、查询并同步个人知识库。来源：`raw/sources/2026-06-22-personal-llm-wiki-skill.md`
- 仓库内置 Codex skill：`skills/personal-llm-wiki`。其他 agent 可以 clone `git@github.com:turen1/knowledge.git` 到任意目录，repo-embedded skill 会自动把 clone 根目录识别为知识库根目录。来源：`raw/sources/2026-06-22-embed-skill-in-knowledge-repo.md`
- PowerShell
- Git
- ffmpeg / ffprobe
- 剪映专业版
- CocosProject 工作区：`G:\CocosProject`

来源：`raw/conversations/2026-06-22-initial-context.md`

## 已知路径

- 视频工作区：`G:\video`
- 黑夜告白项目：`G:\video\heiyegaobai_explain`
- 音色库：`G:\video\音色库`
- 默认知识库：`G:\knowledge`，已恢复为完整 Git 仓库。来源：`raw/conversations/2026-06-26-restore-default-knowledge-path.md`
- 临时知识库 clone：`G:\knowledge_repo`，可作为历史恢复用 clone。来源：`raw/conversations/2026-06-26-record-cocosproject-docs.md`、`raw/conversations/2026-06-26-restore-default-knowledge-path.md`

来源：`raw/conversations/2026-06-22-initial-context.md`

## AI 编码与多模态工具分工

- Codex：适合作为主开发与交付工具，负责实现、重构、测试、构建、文件操作、浏览器/GUI 验证和 Git 流程。
- Claude：适合复杂系统设计、架构审查、代码审查、疑难 Bug 根因分析、GDD/技术设计文档和世界观一致性。
- Gemini：适合截图、录屏、音频、PDF、日志和 Google 技术栈相关任务的多模态分析与批量处理。

来源：`raw/sources/2026-06-26-ai-coding-models-game-development-comparison.md`

## 可沉淀的 Cocos 辅助 skill

`cocos-mentor` 可作为未来项目内 skill：在实现复杂 Cocos Creator 功能前，先强制执行“先提问，再执行”流程，澄清组件解耦、状态管理、持久化、对象池、DrawCall、内存泄漏和验收标准。

来源：`raw/sources/2026-06-26-jikoujiang-ask-before-execute-prompt-video-analysis.md`

## 解说配音音色资产：I 清亮机灵（MiMo 克隆，可跨剧复用）

电视剧解说账号的固定通用男声，首次用于《黑夜告白》讲透版。**下一部解说剧直接复用同一母带克隆即可，音色完全一致。**

- **母带（音色本体）**：本地 `G:\video\音色库\I清亮机灵_母带.wav`（+ `_备份.wav`）；音色卡：`G:\video\音色库\I清亮机灵_音色卡.md`。
- 🔒 **已异地备份进本知识库**：`raw/assets/voice/I清亮机灵_母带.wav`（+ 同目录音色卡），随仓库推送到 GitHub。MD5 `b568576d065e25801f9d1c44a5ad09ff`。任意 clone 本仓库即得母带，可直接做克隆参考。
- ⚠️ **MiMo 是即时克隆，云端无 voice_id —— 音色 = 母带文件本身**。母带丢了无法完全复现（VoiceDesign 有随机性，重生成只得近似），务必本地+云盘+本仓库多处备份，别删别覆盖。
- 特征：年轻男声(约25岁)，清亮透亮、明快干净、机灵小幽默、去播音腔。成片语速 **1.1x**（ffmpeg `atempo=1.1`，不变调）。
- 来源：MiMo VoiceDesign（`mimo-v2.5-tts-voicedesign`）生成，原始描述 prompt 见音色卡/raw。
- 复用/补录：克隆模型 `mimo-v2.5-tts-voiceclone`，读母带 base64 作 voice 参考、文本放 assistant 逐段合成 → `atempo=1.1` 变速 → 拼接。直接改脚本 `heiyegaobai_explain\scripts\mimo_tts_batch_v2.py` 的 REF 路径+换分段稿。补录新句须用同一母带+1.1x+同后处理+响度归一，并听插入接缝。
- API：`https://api.xiaomimimo.com/v1`，密钥环境变量 `MIMO_API_KEY`。完整方法论：`G:\video\解说配音_MiMo音色克隆SOP.md`。

来源：`raw/conversations/2026-06-22-解说配音音色资产-i清亮机灵(mimo克隆).md`
