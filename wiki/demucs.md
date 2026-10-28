# Demucs 与背景音乐分离

## 是什么，什么时候需要

Demucs 是开源音源分离工具，最初由 Meta 研究团队开发。它通过预训练模型，从混合音频中估计人声、鼓、贝斯和其他声部。适用于提取伴奏、去除人声或获得单独声部等需求。

| 需求 | 常用处理 | 得到的结果 |
|---|---|---|
| 把视频声音单独保存 | FFmpeg 提取音轨 | 原音轨中的音乐、人声、音效全部保留 |
| 去掉人声，尽量保留伴奏 | Demucs 等音源分离工具 | 模型估计的非人声声部 |
| 单独提取人声 | Demucs 等音源分离工具 | 模型估计的人声声部 |

视频中的人声和音乐通常已经混合，无法仅靠“另存为音频”把它们拆开。本次用户明确要求去掉说话声，所以在提取音轨后使用了 Demucs。

来源：`raw/conversations/2026-10-28-demucs-bgm-separation.md`；[Demucs 官方项目](https://github.com/facebookresearch/demucs)。

## 与 Python 的关系

Python 是编程语言，Demucs 是用 Python 开发的音源分离工具。使用 Python 可以调用 Demucs，也可以调用其他工具和模型。改用 Python 脚本本身不会自动免除依赖安装和模型下载。

| 替代工具或方法 | 用途与限制 |
|---|---|
| audio-separator | Python 包和命令行工具，可调用 MDX-Net、RoFormer、Demucs 等多种模型，适合脚本和批量处理 |
| Spleeter | 基于 Python / TensorFlow 的音源分离工具，提供预训练模型 |
| Ultimate Vocal Remover，简称 UVR | 提供图形界面的音源分离软件，适合手动选择素材和模型 |
| 滤波、左右声道相减 | 不依赖 AI 模型，但适用条件有限；人声与音乐频率重叠时容易同时损伤音乐，不能保证分离效果 |

应根据实际素材试听比较，不把某个工具或模型视为所有素材上的最佳选择。

来源：`raw/conversations/2026-10-28-demucs-bgm-separation.md`；[audio-separator](https://github.com/nomadkaraoke/python-audio-separator)、[Spleeter](https://github.com/deezer/spleeter)、[UVR](https://github.com/Anjok07/ultimatevocalremovergui)。

## 本次验证过的处理流程

2026-10-28 的微博视频任务采用以下流程：

1. 用 yt-dlp 下载可用的最高画质视频。
2. 用 FFmpeg 提取原音轨，并转换为模型可读的 WAV。
3. 用 Demucs 4.0.1 的 htdemucs 模型在 CPU 上分离人声与非人声。
4. 将 `no_vocals.wav` 导出为 320 kbps MP3 和 24 位 PCM WAV。
5. 检查解码、时长、采样数、有效数值和非静音状态。若要判断人声残留、音效保留及音乐损伤，还需试听。
6. 按此次约定清理临时环境、模型和中间文件，保留原视频与背景音乐成品。

本次使用 Python 3.12、CPU 版 PyTorch / torchaudio 2.5.1。以下命令是本次参数示例，执行前须已具备环境、模型及输入文件，不是安装命令：

```powershell
python -m demucs -n htdemucs -d cpu --two-stems vocals --float32 --shifts 1 --overlap 0.25 -j 0 -o separated input.wav
```

其中 `--two-stems vocals` 输出人声和非人声两份文件；本次版本的非人声结果由其他声部合成。`--float32` 控制分离中间结果的格式，不代表能够恢复压缩源文件中已经丢失的细节。

本次约 71 秒视频已完成处理，但仅通过文件和信号层面的校验，没有独立主观试听结论。

来源：`raw/conversations/2026-10-28-demucs-bgm-separation.md`；[Demucs 4.0.1 分离入口源码](https://raw.githubusercontent.com/facebookresearch/demucs/v4.0.1/demucs/separate.py)。

## 效果边界

- 分离结果是模型估计，可能残留说话声，或损伤音乐并产生伪影。
- 去除人声也可能移除歌曲中的演唱，不能默认只移除解说而保留歌声。
- 非人声结果仍可能包含音效和环境声，`no_vocals` 不保证等于纯 BGM。
- WAV 可以避免再次有损编码；高码率 MP3 只能减轻再次编码造成的损失。两者都不能恢复原始音源已经丢失的细节。

来源：`raw/conversations/2026-10-28-demucs-bgm-separation.md`；[Demucs 官方项目](https://github.com/facebookresearch/demucs)。

## 安装与复用状态

截至本次任务结束，临时安装的 Demucs、依赖和 htdemucs 模型均已删除。下次若没有其他可用环境，需要重新准备。

长期保留独立环境和模型能够避免重复安装、下载。将它们保存在 D 盘固定目录只是此前的建议，用户尚未确认执行。此次知识入库不包含安装授权，也不能把此前临时安装的许可扩展为今后自动安装。

相关页面：[[tools]]、[[workflows]]、[[provenance]]。

来源：`raw/conversations/2026-10-28-demucs-bgm-separation.md`。
