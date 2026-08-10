# 项目地图

## 视频项目：黑夜告白讲透版

路径：`G:\video\heiyegaobai_explain`

已知工作内容：

- 拉片产物清理
- 画面层批处理
- 取片切条
- 剪映草稿生成
- 一键合成成片
- 解说配音（MiMo 克隆音色 I清亮机灵，分段 TTS）

配音音色资产「I清亮机灵」可跨剧复用，详见 `wiki/tools.md`。

来源：`raw/conversations/2026-06-22-initial-context.md`、`raw/conversations/2026-06-22-解说配音音色资产-i清亮机灵(mimo克隆).md`

## 玫瑰颂积分商城

本地路径：`D:\phpstudy_pro\WWW\meiguisong-mini`（admin-system 后端与 mini-program 小程序两个独立仓库）

线上服务器连接方式：

- SSH：`ssh jpgy`（即 `root@8.134.74.163:22`，密钥认证，别名配置于 `C:\Users\Syj15\.ssh\config`）
- 站点目录：`/www/meiguisong-mini/`，服务器系统 CentOS 7
- 服务器代码分支：master（2026-08-10 确认，此前为 v2）
- 域名：`https://admin.meiguisong888.com`（后台）、`https://api.meiguisong888.com`（接口）
- 另一台别名 `erp`（`8.134.11.16`）的服务器与本项目无关

来源：`raw/conversations/2026-08-10-meiguisong-production-server.md`

## 个人知识库

仓库：`git@github.com:turen1/knowledge.git`

目标：记录关于用户的一切，并按 LLM Wiki 模式长期维护。

来源：`raw/conversations/2026-06-22-initial-context.md`

## Cocos 游戏项目

当前工作区：`G:\CocosProject`

可复用 AI 工作流：

- 开发复杂 Cocos Creator 功能前，使用“先提问，再执行”流程澄清架构边界。
- 重点提问组件解耦方式、数据结构、持久化、安全校验、同屏节点数量、对象池需求、DrawCall 和内存泄漏风险。
- 可沉淀项目专属 `cocos-mentor` skill，让 AI 在写 TypeScript 组件代码前强制完成架构澄清。
- 游戏开发多模型分工可采用：Claude 做架构和审查，Codex 做实现与验证，Gemini 做多模态分析和高吞吐辅助。

来源：`raw/sources/2026-06-26-jikoujiang-ask-before-execute-prompt-video-analysis.md`、`raw/sources/2026-06-26-ai-coding-models-game-development-comparison.md`

## 抖音视频项目

当前工作区：`G:\douyin`

已入库资料：

- 分镜表构建思路：专业分镜表的标准化信息框架、视觉语言、时间与运动、注释系统和预剪辑心法。
- 分镜表构建思路 2：从剧本分析、视觉总谱、镜头拆解、动态指示到施工注释的构建流程。
- 分镜表规则：分镜表字段、判断标准、层级结构、模板示例和不同项目类型的分镜重点。

可复用成果已编译到 `wiki/workflows.md` 的“专业分镜表构建”。

来源：`raw/sources/2026-07-04-storyboard-construction-ideas.md`、`raw/sources/2026-07-04-storyboard-construction-process.md`、`raw/sources/2026-07-04-storyboard-table-rules.md`

