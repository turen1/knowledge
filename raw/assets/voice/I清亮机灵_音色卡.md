# 音色卡 · I 清亮机灵（解说通用男声）

> 这是一个**可跨剧复用**的固定音色。下一部解说剧直接用本卡的母带做克隆参考即可。

## 音色本体（最重要）
- **母带文件**：`G:\video\音色库\I清亮机灵_母带.wav`（+ `_备份.wav`）
- ⚠️ **MiMo 是即时克隆，云端没有 voice_id。音色 = 这个音频文件本身。**
  - 母带**丢了就无法完全复现**（VoiceDesign 有随机性，重生成只能得到近似）。**务必多处备份**（本地+云盘）。
  - 别删、别覆盖。所有"I 音色"都靠它克隆出来。

## 音色特征
- 年轻男声（约 25 岁），清亮透亮、明快干净、偏年轻偏高、不低厚；机灵带点小幽默；口语化、去播音腔。
- 配套语速：成片用 **1.1x**（ffmpeg `atempo=1.1`，不变调）。

## 来源（万一要重生成近似版）
- 方式：MiMo VoiceDesign（`mimo-v2.5-tts-voicedesign`）生成。
- 原始描述：
  > 一个二十五岁左右的年轻中国男生，音色清亮透亮、明快干净，声线偏年轻偏高，一点不低厚，机灵带点小幽默；像对着镜头随口聊天，口语接地气、不做作、没有播音腔；语速快、跳脱利落。

## 下部剧怎么用（三步）
```python
import base64, os
from openai import OpenAI
client = OpenAI(api_key=os.environ["MIMO_API_KEY"], base_url="https://api.xiaomimimo.com/v1")

# 1. 读母带做克隆参考
with open(r"G:\video\音色库\I清亮机灵_母带.wav", "rb") as f:
    voice = "data:audio/wav;base64," + base64.b64encode(f.read()).decode()

# 2. 逐段合成（文本放 assistant）
comp = client.chat.completions.create(
    model="mimo-v2.5-tts-voiceclone",
    messages=[{"role": "user", "content": ""},
              {"role": "assistant", "content": "这一段的解说文本"}],
    audio={"format": "wav", "voice": voice},
)
audio = base64.b64decode(comp.choices[0].message.audio.data)
# 3. 写文件 → ffmpeg atempo=1.1 变速 → 拼接（详见 mimo_tts_batch_v2.py）
```
- 直接复用脚本：`heiyegaobai_explain\scripts\mimo_tts_batch_v2.py`，把 `REF` 改成本母带路径、换分段稿即可。
- 完整方法论见 `解说配音_MiMo音色克隆SOP.md`。

## 一致性说明
只要 REF 始终指向同一个母带文件，**所有剧的配音音色完全一致**（同一声音"主持人"贯穿你的解说账号，利于建立辨识度/人设）。
