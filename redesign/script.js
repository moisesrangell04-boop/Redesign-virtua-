/**
 * Virtua Corretora — Redesign Interactions
 */

document.addEventListener('DOMContentLoaded', () => {

    // ===========================
    // HEADER SCROLL EFFECT
    // ===========================
    const header = document.getElementById('header') || document.querySelector('.header');
    let lastScroll = 0;

    if (header) {
        window.addEventListener('scroll', () => {
            const currentScroll = window.scrollY;
            if (currentScroll > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
            lastScroll = currentScroll;
        });
    }

    // ===========================
    // MOBILE MENU
    // ===========================
    const hamburger = document.getElementById('hamburger');
    const nav = document.getElementById('nav');

    if (hamburger && nav) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            nav.classList.toggle('open');
            document.body.style.overflow = nav.classList.contains('open') ? 'hidden' : '';
        });

        // Close menu on link click
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                nav.classList.remove('open');
                document.body.style.overflow = '';
            });
        });
    }

    // Mobile dropdown toggle
    const dropdownToggles = document.querySelectorAll('.nav-dropdown > .nav-link');
    dropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                toggle.parentElement.classList.toggle('open');
            }
        });
    });

    // ===========================
    // FAQ ACCORDION
    // ===========================
    document.querySelectorAll('.faq-question').forEach(btn => {
        btn.addEventListener('click', () => {
            const item = btn.parentElement;
            const isActive = item.classList.contains('active');

            // Close all
            document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('active'));

            // Toggle current
            if (!isActive) {
                item.classList.add('active');
            }
        });
    });

    // ===========================
    // ANIMATED COUNTERS
    // ===========================
    function animateCounter(el) {
        const target = parseFloat(el.dataset.target);
        const decimals = parseInt(el.dataset.decimals) || 0;
        const duration = 2000;
        const start = 0;
        const startTime = performance.now();

        function update(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);

            // Ease out cubic
            const eased = 1 - Math.pow(1 - progress, 3);
            const current = eased * target;

            if (decimals > 0) {
                el.textContent = current.toFixed(decimals).replace('.', ',');
            } else {
                el.textContent = Math.floor(current).toLocaleString('pt-BR');
            }

            if (progress < 1) {
                requestAnimationFrame(update);
            } else {
                if (decimals > 0) {
                    el.textContent = target.toFixed(decimals).replace('.', ',');
                } else {
                    el.textContent = target.toLocaleString('pt-BR');
                }
            }
        }

        requestAnimationFrame(update);
    }

    // ===========================
    // SCROLL REVEAL
    // ===========================
    const revealElements = document.querySelectorAll('[data-reveal]');
    const counterElements = document.querySelectorAll('.stat-number, .counter-number');
    const animatedCounters = new Set();

    const observerOptions = {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');

                // Trigger counter animation
                entry.target.querySelectorAll('.stat-number, .counter-number').forEach(counter => {
                    if (!animatedCounters.has(counter)) {
                        animatedCounters.add(counter);
                        animateCounter(counter);
                    }
                });
            }
        });
    }, observerOptions);

    revealElements.forEach(el => observer.observe(el));

    // Also observe parent containers for counters
    counterElements.forEach(counter => {
        const parent = counter.closest('[data-reveal]') || counter.closest('.hero-stats');
        if (parent) {
            const counterObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting && !animatedCounters.has(counter)) {
                        animatedCounters.add(counter);
                        animateCounter(counter);
                    }
                });
            }, observerOptions);
            counterObserver.observe(parent);
        }
    });

    // ===========================
    // SMOOTH SCROLL
    // ===========================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // ===========================
    // ACTIVE NAV LINK ON SCROLL
    // ===========================
    const sections = document.querySelectorAll('section[id]');

    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 100;
            if (window.scrollY >= sectionTop) {
                current = section.getAttribute('id');
            }
        });

        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });

    // ===========================
    // FORM SUBMISSION (Demo)
    // ===========================
    const form = document.getElementById('contact-form');
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const btn = form.querySelector('button[type="submit"]');
            const originalText = btn.innerHTML;

            btn.innerHTML = '✅ Enviado com sucesso!';
            btn.style.background = 'var(--green)';
            btn.style.boxShadow = '0 4px 15px rgba(16, 185, 129, 0.35)';

            setTimeout(() => {
                btn.innerHTML = originalText;
                btn.style.background = '';
                btn.style.boxShadow = '';
                form.reset();
            }, 3000);
        });
    }

    // ===========================
    // HERO COUNTERS INIT (visible on load)
    // ===========================
    const heroStats = document.querySelector('.hero-stats');
    if (heroStats) {
        setTimeout(() => {
            heroStats.querySelectorAll('.stat-number').forEach(counter => {
                if (!animatedCounters.has(counter)) {
                    animatedCounters.add(counter);
                    animateCounter(counter);
                }
            });
        }, 800);
    }

    // ===========================
    // QUOTE MODAL & PIPEDRIVE INTEGRATION
    // ===========================
    function initQuoteModal() {
        // 1. Inject Modal HTML into the DOM
        const modalHTML = `
            <div class="quote-modal-overlay" id="quoteModalOverlay">
                <div class="quote-modal">
                    <button class="quote-modal-close" id="quoteModalClose" aria-label="Fechar">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="18" y1="6" x2="6" y2="18"></line>
                            <line x1="6" y1="6" x2="18" y2="18"></line>
                        </svg>
                    </button>
                    <div class="quote-modal-header">
                        <h2 class="quote-modal-title">Solicitar Cotação</h2>
                        <p class="quote-modal-desc">Preencha os dados abaixo e entraremos em contato rapidamente.</p>
                    </div>
                    <form class="quote-modal-form" id="quoteModalForm">
                        <div class="form-group">
                            <input type="text" id="modalName" placeholder="Seu nome completo" required>
                        </div>
                        <div class="form-group">
                            <input type="tel" id="modalPhone" placeholder="Seu WhatsApp" required>
                        </div>
                        <div class="form-group">
                            <input type="email" id="modalEmail" placeholder="Seu e-mail">
                        </div>
                        <div class="form-group">
                            <select id="modalProduct" required>
                                <option value="" disabled selected>Selecione o produto de interesse</option>
                                <option value="Saúde">Plano de Saúde</option>
                                <option value="Odontológico">Plano Odontológico</option>
                                <option value="Vida">Seguro de Vida</option>
                                <option value="Auto">Seguro Auto</option>
                                <option value="Viagem">Seguro Viagem</option>
                                <option value="Residencial">Seguro Residencial</option>
                                <option value="Empresarial">Planos Empresariais</option>
                                <option value="Outro">Outro</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <textarea id="modalMessage" placeholder="Conte-nos sua necessidade (opcional)" rows="3"></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary btn-lg">
                            Enviar Solicitação →
                        </button>
                        <p class="quote-modal-note">Seus dados estão seguros conosco.</p>
                    </form>
                </div>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', modalHTML);

        const overlay = document.getElementById('quoteModalOverlay');
        const btnClose = document.getElementById('quoteModalClose');
        const modalForm = document.getElementById('quoteModalForm');

        // 2. Open Modal Logic
        function openModal(e) {
            e.preventDefault();
            overlay.classList.add('active');
            document.body.style.overflow = 'hidden';

            // Try to pre-select product based on page context
            const pageTitle = document.title.toLowerCase();
            const productSelect = document.getElementById('modalProduct');

            if (pageTitle.includes('saúde')) productSelect.value = 'Saúde';
            else if (pageTitle.includes('odonto')) productSelect.value = 'Odontológico';
            else if (pageTitle.includes('vida')) productSelect.value = 'Vida';
            else if (pageTitle.includes('auto')) productSelect.value = 'Auto';
            else if (pageTitle.includes('viagem')) productSelect.value = 'Viagem';
            else if (pageTitle.includes('residencial')) productSelect.value = 'Residencial';
            else if (pageTitle.includes('frota') || pageTitle.includes('garantia') || pageTitle.includes('estágio')) productSelect.value = 'Empresarial';
        }

        // 3. Close Modal Logic
        function closeModal() {
            overlay.classList.remove('active');
            document.body.style.overflow = '';
        }

        btnClose.addEventListener('click', closeModal);
        overlay.addEventListener('click', (e) => {
            if (e.target === overlay) closeModal();
        });

        // Attach event to all triggering buttons
        document.querySelectorAll('.open-quote-modal').forEach(btn => {
            btn.addEventListener('click', openModal);
        });

        // 4. Form Submission & Pipedrive Integration Boilerplate
        modalForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const submitBtn = modalForm.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;

            submitBtn.innerHTML = 'Enviando...';
            submitBtn.disabled = true;

            const leadData = {
                name: document.getElementById('modalName').value,
                phone: document.getElementById('modalPhone').value,
                email: document.getElementById('modalEmail').value,
                product: document.getElementById('modalProduct').value,
                message: document.getElementById('modalMessage').value,
                source: 'Site Virtua Corretora'
            };

            console.log('Dados do Lead prontos para o Pipedrive:', leadData);

            // ==========================================
            // PIPEDRIVE INTEGRATION 
            // Replace the URL with your Pipedrive Webhook / Zapier / Make endpoint
            // ==========================================
            /*
            try {
                const response = await fetch('YOUR_PIPEDRIVE_WEBHOOK_URL_HERE', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(leadData)
                });
                if (!response.ok) throw new Error('Erro ao enviar');
            } catch (error) {
                console.error('Erro na integração:', error);
            }
            */

            // Simulate successful API call
            setTimeout(() => {
                submitBtn.innerHTML = '✅ Recebemos seu pedido!';
                submitBtn.style.background = 'var(--green)';
                submitBtn.style.boxShadow = '0 4px 15px rgba(16, 185, 129, 0.35)';

                setTimeout(() => {
                    closeModal();
                    // Reset
                    setTimeout(() => {
                        submitBtn.innerHTML = originalText;
                        submitBtn.style.background = '';
                        submitBtn.style.boxShadow = '';
                        submitBtn.disabled = false;
                        modalForm.reset();
                    }, 300);
                }, 2000);
            }, 1000);
        });
    }

    // ===========================
    // CONTACT MODAL (WhatsApp & Call)
    // ===========================
    function initContactModal() {
        const modalHTML = `
            <div class="quote-modal-overlay" id="contactModalOverlay">
                <div class="quote-modal" style="max-width: 450px; text-align: center;">
                    <button class="quote-modal-close" id="contactModalClose" aria-label="Fechar">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="18" y1="6" x2="6" y2="18"></line>
                            <line x1="6" y1="6" x2="18" y2="18"></line>
                        </svg>
                    </button>
                    <div class="quote-modal-header" style="margin-bottom: 24px;">
                        <h2 class="quote-modal-title" style="font-size: 28px;">Nossos Contatos</h2>
                        <p class="quote-modal-desc">Estes números funcionam tanto para ligações quanto para WhatsApp.</p>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 16px;">
                        <a href="https://wa.me/5522999404840" target="_blank" class="btn" style="display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 18px; padding: 14px; color: var(--primary); border: 2px solid var(--primary); background: transparent; border-radius: var(--radius-full); text-decoration: none; font-weight: 600; width: 100%;">
                            📞 (22) 99940-4840
                        </a>
                        <a href="https://wa.me/5522995172733" target="_blank" class="btn" style="display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 18px; padding: 14px; color: var(--primary); border: 2px solid var(--primary); background: transparent; border-radius: var(--radius-full); text-decoration: none; font-weight: 600; width: 100%;">
                            📞 (22) 99517-2733
                        </a>
                        <a href="https://wa.me/5522998811541" target="_blank" class="btn" style="display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 18px; padding: 14px; color: var(--primary); border: 2px solid var(--primary); background: transparent; border-radius: var(--radius-full); text-decoration: none; font-weight: 600; width: 100%;">
                            📞 (22) 99881-1541
                        </a>
                    </div>
                </div>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', modalHTML);

        const overlay = document.getElementById('contactModalOverlay');
        const btnClose = document.getElementById('contactModalClose');

        function openModal(e) {
            e.preventDefault();
            overlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeModal() {
            overlay.classList.remove('active');
            document.body.style.overflow = '';
        }

        if (btnClose) btnClose.addEventListener('click', closeModal);
        if (overlay) overlay.addEventListener('click', (e) => {
            if (e.target === overlay) closeModal();
        });

        document.querySelectorAll('.open-contact-modal').forEach(btn => {
            btn.addEventListener('click', openModal);
        });
    }

    initQuoteModal();
    initContactModal();
});
