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

# Find ALL chapter headings (including subsections)
all_headings = list(re.finditer(r'## 第(\d+)章 (.+?)(?=\n|$)', content))

# Group by chapter number - take the first occurrence of each chapter number
# and combine all content until the next distinct chapter number
chapters = {}
for match in all_headings:
    chapter_num = int(match.group(1))
    if chapter_num not in chapters:
        chapters[chapter_num] = {
            'title': match.group(2).strip(),
            'start': match.start()
        }

# Sort by chapter number
sorted_chapters = sorted(chapters.items())

# Extract content for each chapter
for i, (chapter_num, chapter_info) in enumerate(sorted_chapters):
    start_pos = chapter_info['start']
    
    # End position is the start of the next chapter (or end of file)
    if i + 1 < len(sorted_chapters):
        end_pos = sorted_chapters[i + 1][1]['start']
    else:
        end_pos = len(content)
    
    # Extract chapter content
    chapter_content = content[start_pos:end_pos]
    
    # Remove the chapter header(s) from content - keep only the first one
    lines = chapter_content.split('\n')
    first_heading_found = False
    filtered_lines = []
    for line in lines:
        if line.startswith('## 第') and not first_heading_found:
            first_heading_found = True
            continue  # Skip the first chapter heading
        filtered_lines.append(line)
    
    chapter_content = '\n'.join(filtered_lines)
    
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
    
    # Generate active states for sidebar
    active_states = {}
    for n in range(1, 14):
        active_states[f'active{n}'] = 'class="active"' if n == chapter_num else ''
    
    # HTML template
    html_template = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>第{chapter_num}章 {chapter_info['title']} - Solon-AI 学习手册</title>
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
                    <li><a href="01.html" {active_states['active1']}>第1章 框架概览与环境搭建</a></li>
                    <li><a href="02.html" {active_states['active2']}>第2章 ChatModel 与 LLM 调用</a></li>
                    <li><a href="03.html" {active_states['active3']}>第3章 提示词工程与对话管理</a></li>
                    <li><a href="04.html" {active_states['active4']}>第4章 工具（Tool）基础</a></li>
                </ul>
            </div>
            <div class="nav-section">
                <h3>第二阶段</h3>
                <ul>
                    <li><a href="05.html" {active_states['active5']}>第5章 RAG 知识库全链路</a></li>
                    <li><a href="06.html" {active_states['active6']}>第6章 Agent 智能体</a></li>
                    <li><a href="07.html" {active_states['active7']}>第7章 MCP 协议深度集成</a></li>
                    <li><a href="08.html" {active_states['active8']}>第8章 AI Flow 低代码编排</a></li>
                    <li><a href="09.html" {active_states['active9']}>第9章 Talents 能力插件体系</a></li>
                </ul>
            </div>
            <div class="nav-section">
                <h3>第三阶段</h3>
                <ul>
                    <li><a href="10.html" {active_states['active10']}>第10章 多智能体协作系统</a></li>
                    <li><a href="11.html" {active_states['active11']}>第11章 企业级 RAG 应用</a></li>
                    <li><a href="12.html" {active_states['active12']}>第12章 MCP 网关与服务治理</a></li>
                    <li><a href="13.html" {active_states['active13']}>第13章 综合项目实战：智能客服平台</a></li>
                </ul>
            </div>
        </nav>
        <div class="sidebar-footer">
            <p><a href="../index.html" style="color: inherit;">← 返回首页</a></p>
        </div>
    </aside>
    <main class="main-content">
        <div class="content-wrapper">
            {html_content}
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
    
    # Write to file
    output_path = f'/Users/deane/Documents/workspace-java/solon-ai/handbook/chapters/{chapter_num:02d}.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    print(f'✓ Generated chapter {chapter_num:02d}: {chapter_info["title"]}')

print(f'\n✅ Generated {len(sorted_chapters)} chapters successfully!')
print(f'   Output directory: /Users/deane/Documents/workspace-java/solon-ai/handbook/chapters/')
