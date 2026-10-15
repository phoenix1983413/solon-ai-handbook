# Solon-AI 学习手册

> **从入门到进阶的完整学习路径** | 基于 Solon-AI 4.1.1

[![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-blue)](https://pages.github.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## 📖 在线访问

🌐 **GitHub Pages**: [https://your-username.github.io/solon-ai-handbook](https://your-username.github.io/solon-ai-handbook)

*请将 `your-username` 替换为你的 GitHub 用户名*

---

## 🚀 快速部署到 GitHub Pages

### 步骤 1：创建 GitHub 仓库

```bash
# 在 GitHub 上创建新仓库：solon-ai-handbook
# 仓库类型：Public
# 不要初始化 README、.gitignore 或 License
```

### 步骤 2：本地配置远程仓库

```bash
cd /Users/deane/Documents/workspace-java/solon-ai

# 添加远程仓库（替换为你的仓库地址）
git remote add origin https://github.com/your-username/solon-ai-handbook.git

# 推送代码
git branch -M main
git push -u origin main
```

### 步骤 3：启用 GitHub Pages

1. 进入仓库 **Settings** → **Pages**
2. **Source** 选择：`Deploy from a branch`
3. **Branch** 选择：`main` / `handbook`（或 `gh-pages`）
4. 点击 **Save**
5. 等待 2-5 分钟，访问 `https://your-username.github.io/solon-ai-handbook`

### 步骤 4：自定义域名（可选）

在仓库根目录创建 `CNAME` 文件：

```bash
echo "your-domain.com" > CNAME
git add CNAME
git commit -m "chore: add custom domain"
git push
```

然后在域名 DNS 中添加 CNAME 记录指向 `your-username.github.io`

---

## 📚 文档结构

```
handbook/
├── index.html              # 首页（学习路径总览）
├── css/
│   └── style.css           # 全局样式
├── js/
│   └── app.js              # 导航、搜索、交互逻辑
├── chapters/
│   ├── 01.html             # 第1章 框架概览与环境搭建
│   ├── 02.html             # 第2章 ChatModel 与 LLM 调用
│   ├── 03.html             # 第3章 提示词工程与对话管理
│   ├── 04.html             # 第4章 工具（Tool）基础
│   ├── 05.html             # 第5章 RAG 知识库全链路
│   ├── 06.html             # 第6章 Agent 智能体
│   ├── 07.html             # 第7章 MCP 协议深度集成
│   ├── 08.html             # 第8章 AI Flow 低代码编排
│   ├── 09.html             # 第9章 Talents 能力插件体系
│   ├── 10.html             # 第10章 多智能体协作系统
│   ├── 11.html             # 第11章 企业级 RAG 应用
│   ├── 12.html             # 第12章 MCP 网关与服务治理
│   └── 13.html             # 第13章 综合项目实战
└── assets/                 # 图片、图标等静态资源
```

---

## 🎯 学习路径

### 第一阶段：基础入门（1-4章）
- 第1章：框架概览与环境搭建
- 第2章：ChatModel 与 LLM 调用
- 第3章：提示词工程与对话管理
- 第4章：工具（Tool）基础

**预计耗时**：1-2 周

### 第二阶段：核心进阶（5-9章）
- 第5章：RAG 知识库全链路
- 第6章：Agent 智能体（ReAct + Team）
- 第7章：MCP 协议深度集成
- 第8章：AI Flow 低代码编排
- 第9章：Talents 能力插件体系

**预计耗时**：2-3 周

### 第三阶段：高级实战（10-13章）
- 第10章：多智能体协作系统
- 第11章：企业级 RAG 应用
- 第12章：MCP 网关与服务治理
- 第13章：综合项目实战：智能客服平台

**预计耗时**：1-2 周

---

## ✨ 特性

- 📱 **响应式设计**：支持桌面、平板、手机访问
- 🌙 **暗色模式**：自动适配系统主题
- 🔍 **全文搜索**：按 `Ctrl+K`（Mac: `Cmd+K`）快速搜索章节
- 💻 **代码高亮**：集成 highlight.js，支持 100+ 编程语言
- 📑 **侧边栏导航**：清晰的章节结构，一目了然
- ⚡ **快速加载**：纯静态站点，CDN 加速

---

## 🛠️ 本地开发

### 环境要求

- **Node.js**：16+（可选，用于本地服务器）
- **Python**：3.7+（用于生成章节）

### 安装依赖

```bash
cd handbook
npm install
```

### 启动本地服务器

```bash
# 方法1：使用 Python
python3 -m http.server 8080

# 方法2：使用 Node.js
npx serve .
```

### 重新生成章节

如果修改了 `docs/learning-guide.md`，需要重新生成 HTML：

```bash
python3 generate.py
git add handbook/chapters/
git commit -m "docs: regenerate chapters"
git push
```

---

## 📝 更新内容

修改 `docs/learning-guide.md` 后：

```bash
# 1. 重新生成 HTML
cd handbook && python3 generate.py

# 2. 提交更改
cd ..
git add .
git commit -m "docs: update learning guide"
git push

# 3. GitHub Actions 会自动部署（约 2 分钟）
```

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'feat: add amazing feature'`)
4. 推送分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

---

## 📄 许可证

MIT License © 2026

---

## 🔗 相关链接

- [Solon-AI 官方文档](https://solon.noear.org/article/learn-solon-ai)
- [Solon-AI GitHub](https://github.com/opensolon/solon-ai)
- [Solon 框架官网](https://solon.noear.org)
- [MCP 协议规范](https://modelcontextprotocol.io)

---

## 💡 学习建议

1. **循序渐进**：不要跳章学习，每个阶段的练习都要亲手完成
2. **代码先行**：先运行示例代码，再理解原理
3. **多做笔记**：建议使用 Notion/Obsidian 记录学习心得
4. **参与社区**：遇到问题先在 GitHub Issues 搜索，没有则提交
5. **实战驱动**：第13章的综合项目建议完整实现一遍

---

**祝你学习愉快！** 🎉
