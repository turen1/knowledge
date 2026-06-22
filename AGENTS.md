# Knowledge Base Agent Instructions

所有输出和提交说明优先使用中文。

这个仓库是用户的个人 LLM Wiki。维护时必须遵守以下规则。

## 总原则

- `raw/` 是事实来源区：只追加，不改写，不删除，除非用户明确要求。
- `wiki/` 是编译区：可以重写、合并、拆分、交叉引用，但不得编造事实。
- `wiki/` 里的个人事实必须有来源，优先引用 `raw/...` 文件。
- 如果事实来自当前对话，先把对话摘要写入 `raw/conversations/`，再编译进 `wiki/`。
- 不确定的信息写入 `wiki/open-questions.md`，不要强行推断。
- 隐私敏感内容要标注敏感级别，不要无来源扩写。
- 每次更新后必须运行 `python scripts/audit_kb.py`，然后 `git add`、`git commit`、`git push`。

## 文件分层

### raw/

保存原始资料：

- 用户明确说过的话
- 项目交接文档摘要
- 对话摘要
- 文章、网页、PDF、笔记、截图说明

命名建议：

```text
raw/conversations/YYYY-MM-DD-topic.md
raw/sources/YYYY-MM-DD-source-name.md
raw/projects/YYYY-MM-DD-project-name.md
```

### wiki/

保存编译后的页面：

- `index.md`：总入口
- `profile.md`：用户画像
- `preferences.md`：偏好和工作方式
- `projects.md`：项目地图
- `workflows.md`：常用工作流
- `tools.md`：工具和环境
- `timeline.md`：时间线
- `open-questions.md`：待确认问题
- `provenance.md`：来源索引

## 写作要求

- 用清晰的事实句，不写营销腔。
- 重要断言后面写来源，例如：`来源：raw/conversations/2026-06-22-initial-context.md`。
- 不要把“推测”写成事实。
- 可用 `置信度：高/中/低` 标注不稳定信息。
- 每次更新尽量补充反向链接。

## 更新流程

1. 读取新增 `raw/`。
2. 判断哪些 `wiki/` 页面受影响。
3. 更新对应页面和 `wiki/provenance.md`。
4. 将不确定项写入 `wiki/open-questions.md`。
5. 运行审计脚本。
6. 提交并推送到 GitHub。

