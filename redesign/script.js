/**
 * Virtua Corretora — Redesign Interactions
 */

document.addEventListener('DOMContentLoaded', () => {

    // ===========================
    // HEADER SCROLL EFFECT
    // ===========================
    const header = document.getElementById('header');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.scrollY;
        if (currentScroll > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
        lastScroll = currentScroll;
    });

    // ===========================
    // MOBILE MENU
    // ===========================
    const hamburger = document.getElementById('hamburger');
    const nav = document.getElementById('nav');

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
        const target = parseInt(el.dataset.target);
        const duration = 2000;
        const start = 0;
        const startTime = performance.now();

        function update(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);

            // Ease out cubic
            const eased = 1 - Math.pow(1 - progress, 3);
            const current = Math.floor(eased * target);

            el.textContent = current.toLocaleString('pt-BR');

            if (progress < 1) {
                requestAnimationFrame(update);
            } else {
                el.textContent = target.toLocaleString('pt-BR');
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
});
