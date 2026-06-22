# 概念库

这里记录用户关注的概念、方法论和术语解释。

## 驾驭工程

“驾驭工程”是把 AI 当成一个可协作、可调度、可验收的执行系统来使用的一整套方法。它不只关注如何写提示词，还关注任务拆解、上下文组织、约束设置、工具调用、多 agent 分工、结果验证、中断恢复、失败重试，以及如何把 AI 接入真实工作流。

来源：`raw/conversations/2026-06-22-driving-engineering-vs-prompt-engineering.md`

## 提示词工程

“提示词工程”主要研究如何写 prompt，让模型给出更好的回答。它是驾驭工程的一部分，但不是全部。

来源：`raw/conversations/2026-06-22-driving-engineering-vs-prompt-engineering.md`

## 两者区别

提示词工程更像是“会问 AI”，驾驭工程更像是“会用 AI 干活”。

对比：

| 维度 | 提示词工程 | 驾驭工程 |
|---|---|---|
| 核心对象 | 一次模型回答 | 一个完整任务系统 |
| 关注点 | prompt 写法 | 任务拆解、工具调用、流程控制、验收 |
| 典型产物 | 提示词模板 | 自动化流程、脚本、agent 协作、校验机制 |
| 适用场景 | 问答、写作、总结、生成 | 编程、批处理、数据处理、长任务、复杂项目 |
| 成败标准 | 回答质量 | 任务是否真的完成、可复现、可验收 |

来源：`raw/conversations/2026-06-22-driving-engineering-vs-prompt-engineering.md`

## 用户当前实践

用户近期使用交接文档定义任务，用约束控制范围，用脚本和工具落地，用校验报告验收结果。这种使用方式已经超出单纯提示词工程，更接近驾驭工程。

来源：`raw/conversations/2026-06-22-driving-engineering-vs-prompt-engineering.md`

