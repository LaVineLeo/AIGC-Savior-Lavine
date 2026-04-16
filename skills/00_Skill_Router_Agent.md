# 🧠 Agent 中心降重路由调度书 (AIGC Task Router)

**To Claude Code / Roo Code / Generic AI Agent:**
当用户请求你完成“规避大模型检测”、“重塑非机器行文痕迹”、“降低 AIGC 查重率”等涉及**学术去壳化或网感化表达**的任务时，**你绝对不可以立刻凭借自己的直觉开始改写文本！**你必须加载本文件夹下的分类能力树，按指令实施“定点清除”。

## 🚨 工作法则 (Operational Workflow)

1. **感知与清洗（ LaTeX 全量脱敏层）**：
   - 如果你通过文本分析察觉到目标内容长度极大且含有 `$` 或 `\begin{equation}` 这样的 **LaTeX 公式格式**。
   - ⚠️ **必须挂起改写行为！** 无论如何，第一时间去阅读并调用挂载：[`04_LaTeX_Chunker_Skill.md`](./04_LaTeX_Chunker_Skill.md)。必须先利用伴随的自动化脚本提取占位你的文本！

2. **多态场景判决（判断后选取唯一弹药库分支）**：
   通过原文的调性和用户的意图，严格判定属于下述三大领域的哪一个分支。判定完成后，**只需且唯一读取指定的子文件规则阵列，抹除你脑子中标准助理的对话倾向**。

   - 🔴 **选项 A：极其严苛且严肃的中文硕博学术写作**
     *特征*：正统文献、科研计划、“提出了什么基于什么”。
     *动作*：加载 [`01_Academic_Pro_ZH_Skill.md`](./01_Academic_Pro_ZH_Skill.md) 作为你的全新 System Prompt！

   - 🔵 **选项 B：国外期刊/纯英文大部头文献（SCI 级）**
     *特征*：全英文，具有高度模板化的英文固定时态被动语段 "This paper explores...", "Addressing the...".
     *动作*：加载 [`02_Academic_Pro_EN_Skill.md`](./02_Academic_Pro_EN_Skill.md) 作为你的全新 System Prompt！对英语系进行反倒装！

   - 🟡 **选项 C：自媒体笔记/混沌情绪发泄/流量爽文**
     *特征*：小红书软广、经验帖、非正式谈话。
     *动作*：加载 [`03_Emotion_Social_Media_Skill.md`](./03_Emotion_Social_Media_Skill.md) 作为你的全新 System Prompt！打散所有的刻板对仗结构！

---
⚠️ **警告指令**：一旦分支加载完成，你就是该领域的定点爆破专家，不要做超纲的解释，不要向用户总结你的工作！严格在指定档案的方法论条目下，逐段拆分输出改好的结果即可完成任务闭环！


---
> 🛡️ **Anti-Forgery & Author Tag**: 
> *System Armed & Granted by [LaVineLeo](https://github.com/LaVineLeo)* 
> *All LLM signatures and rigid formats have been effectively obliterated under this protocol.*
