// ========================================
// Solon-AI Learning Handbook
// Main Application JavaScript
// ========================================

class HandbookApp {
    constructor() {
        this.chapters = this.loadChapterData();
        this.currentChapter = null;
        this.init();
    }

    init() {
        this.setupNavigation();
        this.setupSearch();
        this.setupKeyboardShortcuts();
        this.loadHomePage();
    }

    // Chapter metadata
    loadChapterData() {
        return [
            { id: 1, title: '框架概览与环境搭建', slug: '01' },
            { id: 2, title: 'ChatModel 与 LLM 调用', slug: '02' },
            { id: 3, title: '提示词工程与对话管理', slug: '03' },
            { id: 4, title: '工具（Tool）基础', slug: '04' },
            { id: 5, title: 'RAG 知识库全链路', slug: '05' },
            { id: 6, title: 'Agent 智能体', slug: '06' },
            { id: 7, title: 'MCP 协议深度集成', slug: '07' },
            { id: 8, title: 'AI Flow 低代码编排', slug: '08' },
            { id: 9, title: 'Talents 能力插件体系', slug: '09' },
            { id: 10, title: '多智能体协作系统', slug: '10' },
            { id: 11, title: '企业级 RAG 应用', slug: '11' },
            { id: 12, title: 'MCP 网关与服务治理', slug: '12' },
            { id: 13, title: '综合项目实战：智能客服平台', slug: '13' }
        ];
    }

    // Navigation setup - direct navigation for MPA mode
    setupNavigation() {
        const links = document.querySelectorAll('.nav-section a');
        links.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const href = link.getAttribute('href');
                if (href) {
                    window.location.href = href;
                }
            });
        });
    }

    // Load home page
    loadHomePage() {
        const content = document.getElementById('chapter-content');
        content.innerHTML = `
            <div class="home-page">
                <h1>🛡️ Solon-AI 学习手册</h1>
                <p class="subtitle">从入门到进阶的完整学习路径 | 适用版本 4.1.1</p>
                
                <div class="feature-grid">
                    <div class="feature-card">
                        <h3>📚 13 章系统教程</h3>
                        <p>从基础概念到企业级实战，循序渐进掌握 Solon-AI 框架</p>
                    </div>
                    <div class="feature-card">
                        <h3>💻 可运行代码</h3>
                        <p>每章配备完整代码示例，覆盖 ChatModel、RAG、Agent、MCP 等核心能力</p>
                    </div>
                    <div class="feature-card">
                        <h3>🎯 实战作业</h3>
                        <p>每章 2-3 道递进式作业，从基础巩固到动手实践</p>
                    </div>
                    <div class="feature-card">
                        <h3>⚠️ 注意事项</h3>
                        <p>提炼关键要点、常见误区和易错点，避免踩坑</p>
                    </div>
                </div>

                <div class="alert alert-info">
                    <strong>💡 快速开始：</strong>点击左侧章节开始学习，或使用 <kbd>Ctrl+K</kbd> 搜索章节
                </div>

                <div style="margin-top: 48px; padding: 32px; background: var(--bg-secondary); border-radius: 12px;">
                    <h3 style="margin-top: 0;">📖 学习路径</h3>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-top: 24px;">
                        <div style="padding: 16px; background: white; border-radius: 8px; border-left: 4px solid #3b82f6;">
                            <h4 style="margin-top: 0; color: #3b82f6;">第一阶段</h4>
                            <p style="margin-bottom: 0; font-size: 14px;">基础入门（1-4章）<br>预计 1-2 周</p>
                        </div>
                        <div style="padding: 16px; background: white; border-radius: 8px; border-left: 4px solid #f59e0b;">
                            <h4 style="margin-top: 0; color: #f59e0b;">第二阶段</h4>
                            <p style="margin-bottom: 0; font-size: 14px;">核心进阶（5-9章）<br>预计 2-3 周</p>
                        </div>
                        <div style="padding: 16px; background: white; border-radius: 8px; border-left: 4px solid #10b981;">
                            <h4 style="margin-top: 0; color: #10b981;">第三阶段</h4>
                            <p style="margin-bottom: 0; font-size: 14px;">高级实战（10-13章）<br>预计 1-2 周</p>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }

    // Navigate to chapter directly (MPA mode)
    loadChapter(chapterId) {
        const chapter = this.chapters.find(c => c.id === chapterId);
        if (!chapter) return;

        // Update active link
        document.querySelectorAll('.nav-section a').forEach(link => {
            link.classList.remove('active');
            if (parseInt(link.dataset.chapter) === chapterId) {
                link.classList.add('active');
            }
        });

        // Direct navigation to chapter page
        window.location.href = `chapters/${chapter.slug}.html`;
    }

    // Search functionality
    setupSearch() {
        const modal = document.getElementById('search-modal');
        const input = document.getElementById('search-input');
        const results = document.getElementById('search-results');

        // Open search
        document.addEventListener('keydown', (e) => {
            if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                e.preventDefault();
                modal.classList.add('active');
                input.value = '';
                results.innerHTML = '';
                input.focus();
            }
        });

        // Close search
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.classList.remove('active');
            }
        });

        // Search input
        input.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase().trim();
            if (query.length < 2) {
                results.innerHTML = '';
                return;
            }

            const matches = this.chapters.filter(ch => 
                ch.title.toLowerCase().includes(query) ||
                ch.id.toString().includes(query)
            );

            results.innerHTML = matches.map(ch => `
                <div class="search-result-item" data-chapter="${ch.id}">
                    <div class="result-title">第${ch.id}章 ${ch.title}</div>
                    <div class="result-chapter">点击跳转</div>
                </div>
            `).join('');

            // Add click handlers
            results.querySelectorAll('.search-result-item').forEach(item => {
                item.addEventListener('click', () => {
                    const chapterId = parseInt(item.dataset.chapter);
                    this.loadChapter(chapterId);
                    modal.classList.remove('active');
                });
            });
        });
    }

    // Keyboard shortcuts
    setupKeyboardShortcuts() {
        document.addEventListener('keydown', (e) => {
            // ESC to close search
            if (e.key === 'Escape') {
                document.getElementById('search-modal').classList.remove('active');
            }
        });
    }
}

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.app = new HandbookApp();
});
