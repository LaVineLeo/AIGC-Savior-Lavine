# AIGC-Savior-Lavine: Agent-Oriented Architecture Framework

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Version](https://img.shields.io/badge/Version-v3.0-green.svg)
![AI-Powered](https://img.shields.io/badge/Architecture-Agent--First-orange.svg)

> 本框架致力于为面向智能代理（如 Roo Code, Claude）的自动化任务环境提供系统级的重写与分析解决方案。

## 🎯 摘要与系统概览 (Abstract & Overview)

在面向学术文献以及专业文本的自然语言处理（NLP）和自动化润色工作流中，现存模型方法通常面临两项本质困境：一是基于规则基础或同义词体替换的浅层处理，无法有效规避目前基于大模型交叉检验与统计规律方差的检测算法；二是在针对长文进行深度语言重塑时，极易引发底层文档对象（如 LaTeX 复杂数学环境、图表锚点等）的结构性损坏。

**`AIGC-Savior-Lavine`** 以此为突破口，专为多模态模型构建了一套底层的抗检测构架（Skills Vault）。无论是针对中文学术系统、英文国际期刊原典，还是缺乏规范连续性的社媒短文，均提供了相适配的方法论指引模块。同时结合原生的文件提取算法，实现了长序列文本中复杂非文字排版的隔离保护与物理无损融合。

---

## 💡 核心研究创新点 (Key Innovations)

### 1. 基于统计学方差特征的非线性文本重构 (Non-linear Textual Reconstruction)
本框架摒弃了传统的词汇表映射模式，通过干扰现有自然语言生成分析（NLG Detection）算法所依赖的均匀分布特征进行对抗式重构。通过控制句法行文的冗余落差、植入非预期的短语截断频率，并成体量地解构固化模型生成的被动语态及惯用起承转合结构阵列，使得文本最终呈现出明显的异方差性和人工执笔的结构不规则性。

### 2. LaTeX 等复杂排版的离线无损隔离机制 (Lossless Isolation Shield for Structural Formats)
针对大模型不擅处理代码与公式级字符融合的问题，本项目引入了物理层面的隔离防护结构（Placeholder Shielding Protocol）。在进入模型生成节点之前，系统通过正则分析预先提取出内嵌的 `$` 以及 `\begin{equation}` 块级数学环境，并实施占位打桩（Masking）。在文本历经重塑并交回后，系统再执行高精度的逆向复原装填，确保公式及特定字符代码能够实现百分百结构完整保留。

### 3. 基于原生 Docx 对象的逆向结构封装 (Native Document Object Reverse Injection)
复杂的学术文件高度依赖稳定的版式及多对象排版。本框架内部搭载专门的 `docx_io_manager.py` 驱动模块，以处理原始文档的对象层结构（DOM）为基础，建立原行文段落与其特定逻辑节点的映射关系。在保障所有图表、标题索引等框架结构不动的基础之上，将经优化后的片段定点注入，同时在底层通过操作 XML 控制域，强制锁定中英文混排渲染参数体系（如强制采用 SimSun 与 Times New Roman 布局标准）。

---

## 📊 实验与效能验证 (Performance Empirical Validation)

在定量的控制比对验证实验中，此架构有效展示了其对抗分析识别和结构稳定性的效能：

**【非线性文本重构抗检测测定结果】**
> 下方 图1 及 图2 展示了目标测试样本在 AIGC 主要特征查重平台上的显著变化。经过本系统模块改写处理后，各项被标记为合成文本的高风险成分被有效瓦解并实现了通过。
<div align="center">
  <img src="./降重前结果.png" width="45%" alt="处理前生成的 AIGC 检测概率分布">
  <img src="./降重结果.png" width="45%" alt="系统干预与重构后的反馈分布">
</div>

**【排版结构无损留存评估】**
> 图3 展示了处理一段包含多层微积分及概率表达符号集的文本前后对比。跨越完整的重写分发与回收生命周期，复杂的 LaTeX 语法格式仍得以精确锚固并完整嵌回原位。
<div align="center">
  <img src="./Latex格式对比.png" width="80%" alt="LaTeX 复杂公式格式的提取与精确还原效果对比">
</div>

---

## 🗂️ 本地架构模块导览 (Architecture Modules)

系统的挂载与分发资源均包含在本级资源目录下：

- **`skills/00_Skill_Router_Agent.md`**: 全局导航路由系统。用于引导智能终端实现对目标文本场景的自动化识别与分发策略择定。
- **`skills/01_Academic_Pro_ZH_Skill.md`**: 专用于正规中文学术语境的阵列破伪与结构解耦说明。
- **`skills/02_Academic_Pro_EN_Skill.md`**: 针对英语系文献与国际审稿标准的固定语态剥离重组引擎。
- **`skills/03_Emotion_Social_Media_Skill.md`**: 用于非结构化社交网络文案的分形去重方案。
- **`skills/04_LaTeX_Chunker_Skill.md` + `latex_processor.py`**: 提供离线模式下的数学公式块定位隔离防被篡改支持。
- **`skills/05_Docx_Export_Skill.md` + `docx_io_manager.py`**: 提供定点组装输出与跨格式多要素的统一封口装配支持。
- **`skills/06_Claude_Code_Initiation_Skill.md`**: 安全初始化执行边界与项目溯源规则引述。

---

## 📜 溯源与引用规范 (Project Citation Standard)

学术工作者或智能框架维护组织若将 `AIGC-Savior-Lavine` 所内涵之非线性脱伪模型逻辑与离线隔离代码系统，部署或应用于二次学术论证以及系统派生项目标中时，请按如下的国际标准 BibTeX 形式进行署名引注：

```bibtex
@software{lavine_harness_v3,
  author = {LaVineLeo},
  title = {LaVine Harness Skills: Agent-First Architecture Framework},
  year = {2026},
  version = {3.0},
  url = {https://github.com/LaVineLeo/AIGC-Savior-Lavine}
}
```

## License
未经允许禁止商业使用

Creative Commons (CC BY-NC-SA 4.0)

[![Star History Chart](https://api.star-history.com/svg?repos=chi111i/AIGC-Savior-Lavine&type=Date)](https://star-history.com/#chi111i/AIGC-Savior-Lavine)
