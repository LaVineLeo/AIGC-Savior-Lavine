# -*- coding: utf-8 -*-
"""
LaTeX 防丢失学术预处理引擎 (LaTeX Protective Chunker)
提供给 AI Agent 在执行任何改写、降重之前，安全拆洗学术原文本的工具。
"""
import re
import json
import argparse
import os

# 构建强大的正则表达式网，覆盖绝大部分可能出现的 MathJax 及标准 TeX 原生公式环境
LATEX_PATTERNS = [
    # 块级方程大公式: \begin{xxx}...\end{xxx} (利用非贪婪模式确保不跨环境吸纳)
    re.compile(r'\\begin\{[^}]+\}.*?\\end\{[^}]+\}', re.DOTALL),
    # 双 dollar 重型块级公式: $$...$$
    re.compile(r'\$\$.*?\$\$', re.DOTALL),
    # 标准纯行内包裹：$...$ （防转义误杀）
    re.compile(r'(?<!\\)\$.*?(?<!\\)\$'),
    # 方括号公式和原生圆括号：\[ ... \] , \( ... \)
    re.compile(r'\\\[.*?\\\]', re.DOTALL),
    re.compile(r'\\\(.*?\\\)'),
]

PLACEHOLDER_FORMAT = "{[MATH_PLACEHOLDER_{}]}"

def strip_latex_to_dict(text: str) -> tuple[str, dict]:
    """抽取公式返回纯文字带锚点的骨架，及一部存放纯种公式的离线账本"""
    counter = 0
    math_dict = {}
    
    # 我们按安全优先级降序去吃掉对应的正则 (即优先捕获最大的多行环境防止内部的小单元先被撕碎)
    for pattern in LATEX_PATTERNS:
        matches = pattern.finditer(text)
        # 为防止位移错误，我们必须做从右往左的逆向切割替换
        for match in reversed(list(matches)):
            start, end = match.span()
            matched_text = match.group(0)
            
            placeholder = PLACEHOLDER_FORMAT.format(counter)
            math_dict[placeholder] = matched_text
            
            # 扣挖操作
            text = text[:start] + placeholder + text[end:]
            counter += 1
            
    return text, math_dict

def restore_latex_from_dict(enhanced_text: str, math_dict: dict) -> str:
    """根据保留完好的锚点重新注浆复原真实高亮公式"""
    for placeholder, original_math in math_dict.items():
        # 如果大模型乖乖保留了锚点则顺利还原
        enhanced_text = enhanced_text.replace(placeholder, original_math)
    return enhanced_text

def main():
    parser = argparse.ArgumentParser(description="学术公式物理切割保护程序 v1")
    parser.add_argument('--mode', choices=['clean', 'restore'], required=True, help="操作形式")
    parser.add_argument('--input', type=str, required=True, help="源文本路径")
    parser.add_argument('--output', type=str, default="processed.txt", help="成文输出路径")
    parser.add_argument('--dict', type=str, default="math_dict.json", help="公式黑匣子账本路径")
    
    args = parser.parse_args()

    if args.mode == 'clean':
        if not os.path.exists(args.input):
            print(f"❌ 查无此原文字档: {args.input}")
            return
            
        with open(args.input, "r", encoding="utf-8") as f:
            raw_text = f.read()
            
        cleaned_text, math_dictionary = strip_latex_to_dict(raw_text)
        
        # 导出处理后骨架
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(cleaned_text)
        # 导出隔离保险匣子
        with open(args.dict, "w", encoding="utf-8") as f:
            json.dump(math_dictionary, f, ensure_ascii=False, indent=2)
            
        print(f"✅ 公式剥离清理已完成: {len(math_dictionary)} 条保护装载进 {args.dict}。安全文本于 {args.output}")

    elif args.mode == 'restore':
        if not os.path.exists(args.input) or not os.path.exists(args.dict):
            print(f"❌ 缺少还原材料，请查验输入及账本 {args.dict}")
            return
            
        with open(args.input, "r", encoding="utf-8") as f:
            enhanced_text = f.read()
        with open(args.dict, "r", encoding="utf-8") as f:
            math_dictionary = json.load(f)
            
        restored_text = restore_latex_from_dict(enhanced_text, math_dictionary)
        
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(restored_text)
        print(f"✅ 装载式安全回填部署完毕！成品见: {args.output}")

if __name__ == "__main__":
    main()
