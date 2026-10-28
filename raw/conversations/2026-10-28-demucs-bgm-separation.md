# Demucs 与视频背景音乐分离：对话和实践记录

日期：2026-10-28
来源：用户与 Codex 的当前对话、任务执行结果、对话中查阅的官方项目资料。
敏感级别：private

## 用户需求与授权

- 用户要求下载微博视频，并单独提取 BGM。
- 用户进一步明确：“去掉说话声，只保留背景音乐”。
- 得知本地缺少音乐分离工具后，用户确认允许在当前项目内临时安装 Demucs 并下载模型，完成后清理工具、模型和临时文件。
- 用户随后询问 Demucs 是什么、为何需要、下次是否需要重装，以及是否可以用 Python 或其他方式分离音频。
- 用户明确要求：“把demucs相关知识添加到知识库”。
- 长期保留工具和模型在 D 盘仅为助手提出的复用建议，用户尚未要求执行，不应记录为已安装或已确定的长期偏好。

## 已完成的实践

- 视频来源：https://weibo.com/tv/show/1034:5358917014978579?from=old_pc_videoshow
- 使用已有的 yt-dlp 下载最高可用版本，视频分辨率为 1440 × 1080，时长约 70.984 秒。
- FFmpeg 先提取原音轨，再转换为模型输入 WAV。直接提取音轨会保留其中的全部声音，不能等同于分离背景音乐。
- 在项目临时环境中使用 Python 3.12、Demucs 4.0.1、CPU 版 PyTorch / torchaudio 2.5.1，以及 htdemucs 模型完成分离。
- 主要参数：`--two-stems vocals --float32 --shifts 1 --overlap 0.25 -j 0 -d cpu`。`OMP_NUM_THREADS` 与 `MKL_NUM_THREADS` 均设为 4。
- 模型输出中的 `no_vocals.wav` 由非人声声部合成，再导出 320 kbps MP3 和 24 位 PCM WAV。
- 校验了视频和 MP3 的解码、输出时长、WAV 的采样数与输入一致、音频非静音且数值有效。没有执行独立的主观试听评价，不应声称人声完全去净或音质完美。
- 交付文件为 `weibo_5358917014978579.mp4`、`weibo_5358917014978579_BGM.mp3`、`weibo_5358917014978579_BGM.wav`。
- 文件保存在 `C:\Users\Syj15\Documents\Codex\2026-10-28\https-weibo-com-tv-show-1034\outputs`。
- 临时环境、依赖、模型、下载缓存、网页和元数据、原始音轨中间文件均已清理，原视频和两份 BGM 保留。此状态为本次任务结束时的记录。

## 对话中确认的知识

- Demucs 是开源音源分离工具，最初由 Meta 研究团队开发。它通过训练好的模型估计混合音频中的人声、鼓、贝斯及其他声部。
- Demucs 本身由 Python 开发。Python 是编程语言，不能与 Demucs 当作同一层级的替代方案比较；Python 可以调用不同的分离工具和模型。
- 去人声属于模型估计，可能存在人声残留、音乐损失和处理伪影，不能保证恢复原始伴奏。音乐中的歌声也可能一起被分离。
- 其他工具包括 Python 的 audio-separator、Spleeter，以及带图形界面的 Ultimate Vocal Remover。audio-separator 可以调用包括 MDX-Net、RoFormer、Demucs 在内的多种模型。
- 普通滤波和左右声道相减不需要 AI 模型，但依赖素材条件，无法普遍解决人声与音乐频率重叠的问题。
- 本次临时安装已删除，下次若继续用 Demucs，且没有其他可用环境，就需要重新安装并下载模型。保留固定环境及模型能避免重复准备，但需要另行确认长期安装安排。

## 官方资料

以下资料在本次对话中已查阅，内容只作摘要，不复制完整文档。

- Demucs：https://github.com/facebookresearch/demucs
- Demucs 4.0.1 分离入口源码：https://raw.githubusercontent.com/facebookresearch/demucs/v4.0.1/demucs/separate.py
- audio-separator：https://github.com/nomadkaraoke/python-audio-separator
- Spleeter：https://github.com/deezer/spleeter
- Ultimate Vocal Remover：https://github.com/Anjok07/ultimatevocalremovergui
