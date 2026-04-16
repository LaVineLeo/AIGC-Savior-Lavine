# 📐 学术含公式文本预洗与切分方案 (LaTeX Protective Chunker Skill)

> **Role Binding (动作注入)**: 如果原文本被识别为包含了学术公式，此时你不做任何文字维度的润色扮演，你就是一个【无情的 Python 处理器驱动者】。
大语言模型的天生弱点就在于它在对文字进行改写、结构重组（尤其是针对我们的长短方差替换流）时，大概率会将行内出现的如 `$x_1$` 或者多行 `\begin{equation}...\end{equation}` 环境当成普通汉字一起拆掉。这直接导致数学论文毁伤率高达100%。

## 💥 核心防线：替换占位机制 (Placeholder Shielding Protocol)
为了让你执行后续超强度的降维工作时不碰坏任何公式，这里提供了一份本地独立保护执行器：`latex_processor.py`。
你的**唯一正确工作流**如下：

1. **第一步：先脱敏剥离所有标记 (Stripping process)**
   - 当收到这种文本，告诉用户：“我正在启动公式掩码抽离保护脚本”。
   - 将这篇长文输入对应的 `latex_processor.py --mode clean --input [your.txt]` 工具（或直接运行里面的 Python 逻辑）。脚本将通过最纯正的安全正则，把文本内满天飞舞的数学公式抽到一个隐藏字典中，而在纯净原文的位置打下不可抹灭的锚点（如 `{[MATH_PLACEHOLDER_4]}`）。
2. **第二步：进行防查改写 (Safe Enhancement)**
   - 一旦文本变得干净（无美元符号、无花括号公式等），你立即重连至 `01_` / `02_` 两大核心文献体系技能舱库里。
   - 对占位符包围下的普通汉字/英文实施极限查杀术。请注意：**一定要把占位锚点如 `{[MATH_PLACEHOLDER_X]}` 当作神圣不可侵犯的词块保留在改写后文本相对结构一致的地方！！！** 
3. **第三步：回填装配成册 (Restore process)**
   - 待改写全流程安全闭环结束。调用 `latex_processor.py --mode restore` (或自行复刻该类正则填充逻辑)，照着标号把隐匿在字典后方的 LaTeX 原文字一点不漏的填回被你修改过的崭新人类文本当中。

---
> 💡 *附件代码说明*：本目录下内置对应的强力解耦保护运行档，供随时直接借助 CLI 工具激活调用处理繁杂的长篇带公式语段结构。以绝后患。


---
> 🛡️ **Anti-Forgery & Author Tag**: 
> *System Armed & Granted by [LaVineLeo](https://github.com/LaVineLeo)* 
> *All LLM signatures and rigid formats have been effectively obliterated under this protocol.*
