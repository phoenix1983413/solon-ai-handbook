#!/usr/bin/env python3
"""
Convert learning-guide.md to HTML chapters for GitHub Pages
"""

import markdown
import re
import os

# Read the markdown file
with open('/Users/deane/Documents/workspace-java/solon-ai/docs/learning-guide.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Split by chapters
# Pattern to match chapter headers
chapter_pattern = r'## ={5,}\n## 第(\d+)章 (.+?)(?=\n## ={5,}|\Z)'

# Find all chapters
matches = list(re.finditer(chapter_pattern, content, re.DOTALL))

# Create HTML template for each chapter
html_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>第{num}章 {title} - Solon-AI 学习手册</title>
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
    <style>
        .chapter-header {{
            background: linear-gradient(135deg, #2563eb, #1d4ed8);
            color: white;
            padding: 48px;
            margin-bottom: 32px;
            border-radius: 12px;
        }}
        .chapter-header h1 {{
            color: white;
            border: none;
            padding: 0;
            margin: 0;
        }}
        .chapter-meta {{
            display: flex;
            gap: 24px;
            margin-top: 16px;
            font-size: 14px;
            opacity: 0.9;
        }}
        .chapter-nav {{
            display: flex;
            justify-content: space-between;
            margin-top: 64px;
            padding-top: 32px;
            border-top: 1px solid var(--border-color);
        }}
        .chapter-nav a {{
            padding: 12px 24px;
            background: var(--bg-secondary);
            border-radius: 8px;
            text-decoration: none;
            color: var(--text-primary);
            font-weight: 500;
            transition: all 0.2s;
        }}
        .chapter-nav a:hover {{
            background: var(--primary-color);
            color: white;
        }}
        .nav-prev {{ text-align: left; }}
        .nav-next {{ text-align: right; }}
    </style>
</head>
<body>
    <aside class="sidebar">
        <div class="sidebar-header">
            <h1>🛡️ Solon-AI</h1>
            <p>学习手册</p>
        </div>
        <nav class="sidebar-nav">
            <div class="nav-section">
                <h3>第一阶段</h3>
                <ul>
                    <li><a href="01.html" {active1}>第1章 框架概览</a></li>
                    <li><a href="02.html" {active2}>第2章 ChatModel</a></li>
                    <li><a href="03.html" {active3}>第3章 提示词工程</a></li>
                    <li><a href="04.html" {active4}>第4章 工具基础</a></li>
                </ul>
            </div>
            <div class="nav-section">
                <h3>第二阶段</h3>
                <ul>
                    <li><a href="05.html" {active5}>第5章 RAG</a></li>
                    <li><a href="06.html" {active6}>第6章 Agent</a></li>
                    <li><a href="07.html" {active7}>第7章 MCP</a></li>
                    <li><a href="08.html" {active8}>第8章 Flow</a></li>
                    <li><a href="09.html" {active9}>第9章 Talents</a></li>
                </ul>
            </div>
            <div class="nav-section">
                <h3>第三阶段</h3>
                <ul>
                    <li><a href="10.html" {active10}>第10章 多Agent</a></li>
                    <li><a href="11.html" {active11}>第11章 企业RAG</a></li>
                    <li><a href="12.html" {active12}>第12章 MCP网关</a></li>
                    <li><a href="13.html" {active13}>第13章 综合实战</a></li>
                </ul>
            </div>
        </nav>
        <div class="sidebar-footer">
            <p><a href="../index.html" style="color: inherit;">← 返回首页</a></p>
        </div>
    </aside>
    <main class="main-content">
        <div class="content-wrapper">
            {content}
            <div class="chapter-nav">
                {prev_link}
                {next_link}
            </div>
        </div>
    </main>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            document.querySelectorAll('pre code').forEach(block => {{
                hljs.highlightElement(block);
            }});
        }});
    </script>
</body>
</html>"""

# Process each chapter
for i, match in enumerate(matches):
    chapter_num = int(match.group(1))
    chapter_title = match.group(2)
    chapter_content = match.group(0)
    
    # Remove the chapter header from content (we'll add our own)
    chapter_content = re.sub(r'^## ={5,}\n## 第\d+章 .+?\n', '', chapter_content, count=1)
    
    # Convert markdown to HTML
    md = markdown.Markdown(extensions=['extra', 'codehilite', 'toc'])
    html_content = md.convert(chapter_content)
    
    # Generate navigation links
    prev_link = ''
    if chapter_num > 1:
        prev_link = f'<a href="{chapter_num-1:02d}.html" class="nav-prev">← 第{chapter_num-1}章</a>'
    else:
        prev_link = '<a href="../index.html" class="nav-prev">← 返回首页</a>'
    
    next_link = ''
    if chapter_num < 13:
        next_link = f'<a href="{chapter_num+1:02d}.html" class="nav-next">第{chapter_num+1}章 →</a>'
    
    # Generate active states
    active_states = {f'active{n}': 'class="active"' if n == chapter_num else '' for n in range(1, 14)}
    
    # Fill template
    html = html_template.format(
        num=chapter_num,
        title=chapter_title,
        content=html_content,
        prev_link=prev_link,
        next_link=next_link,
        **active_states
    )
    
    # Write to file
    output_path = f'/Users/deane/Documents/workspace-java/solon-ai/handbook/chapters/{chapter_num:02d}.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f'✓ Generated chapter {chapter_num:02d}: {chapter_title}')

print('\n✅ All chapters generated successfully!')
print(f'   Output directory: /Users/deane/Documents/workspace-java/solon-ai/handbook/chapters/')
