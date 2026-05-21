/**
 * Virtua Corretora — Redesign Interactions
 */

// ============================================================
// PIPEDRIVE / MAKE / ZAPIER — substitua pela URL do webhook
// ============================================================
const WEBHOOK_URL = 'YOUR_PIPEDRIVE_WEBHOOK_URL_HERE';
// ============================================================

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

        // Close menu on link click (skip dropdown toggles — they open submenus, not pages)
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                if (link.closest('.nav-dropdown') && link.parentElement.classList.contains('nav-dropdown')) {
                    return; // This link opens a submenu; don't close the menu
                }
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
                const parent = toggle.parentElement;
                if(parent.classList.contains('nav-dropdown')) {
                   e.preventDefault();
                   parent.classList.toggle('open');
                }
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
    // FORM SUBMISSION (Fale Conosco)
    // ===========================
    const form = document.getElementById('contact-form');
    if (form) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = form.querySelector('button[type="submit"]');
            const originalText = btn.innerHTML;
            btn.innerHTML = 'Enviando...';
            btn.disabled = true;

            const name = document.getElementById('name') ? document.getElementById('name').value : '';
            const phone = document.getElementById('phone') ? document.getElementById('phone').value : '';
            const email = document.getElementById('email') ? document.getElementById('email').value : '';
            const productSelect = document.getElementById('product');
            const product = productSelect ? productSelect.value : '';
            const message = document.getElementById('message') ? document.getElementById('message').value : '';

            const leadData = {
                name, phone, email, product, message,
                source: 'Site Virtua Corretora (Fale Conosco)',
                page_url: window.location.href,
                page_title: document.title,
                submitted_at: new Date().toISOString()
            };

            // Extras
            if (product) {
                Object.assign(leadData, extractExtraLeadData('contact_', product));
            }

            try {
                const response = await fetch(WEBHOOK_URL, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(leadData)
                });
                if (!response.ok) throw new Error('HTTP ' + response.status);
            } catch (error) {
                console.error('Erro ao enviar form:', error);
                btn.innerHTML = '⚠️ Tente novamente';
                btn.style.background = '#ef4444';
                btn.disabled = false;
                setTimeout(() => {
                    btn.innerHTML = originalText;
                    btn.style.background = '';
                }, 3000);
                return;
            }

            btn.innerHTML = '✅ Enviado com sucesso!';
            btn.style.background = 'var(--green)';
            btn.style.boxShadow = '0 4px 15px rgba(16, 185, 129, 0.35)';

            setTimeout(() => {
                btn.innerHTML = originalText;
                btn.style.background = '';
                btn.style.boxShadow = '';
                btn.disabled = false;
                form.reset();
                // hide fields
                form.querySelectorAll('.extra-fields').forEach(el => el.classList.remove('visible'));
            }, 3000);
        });

        // Setup extra fields wrapper
        const extraContainer = document.getElementById('contact-extra-fields-container');
        if (extraContainer) {
            extraContainer.innerHTML = getExtraFieldsHTML('contact_');
            const productSelect = document.getElementById('product');
            if (productSelect) {
                productSelect.addEventListener('change', () => {
                    form.querySelectorAll('.extra-fields').forEach(el => el.classList.remove('visible'));
                    const p = productSelect.value;
                    if (p) {
                        const target = document.getElementById('contact_fields-' + p);
                        if (target) target.classList.add('visible');
                    }
                    setupExtraFieldsListeners('contact_');
                });
            }
        }

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
    // EXTRA FIELDS LOGIC
    // ===========================
    function ageRangesHTML(prefix) {
        const ranges = [
            ['00 a 18', '00_18'], ['19 a 23', '19_23'], ['24 a 28', '24_28'],
            ['29 a 33', '29_33'], ['34 a 38', '34_38'], ['39 a 43', '39_43'],
            ['44 a 48', '44_48'], ['49 a 53', '49_53'], ['54 a 58', '54_58'],
            ['59+',     '59_plus'],
        ];
        const opts = Array.from({length: 11}, (_, i) => '<option value="' + i + '">' + i + '</option>').join('');
        return ranges.map(([label, sfx]) =>
            '<div class="age-range-item">' +
            '<label class="age-range-label" for="' + prefix + '_' + sfx + '">' + label + '</label>' +
            '<select id="' + prefix + '_' + sfx + '" class="age-range-select">' + opts + '</select>' +
            '</div>'
        ).join('');
    }

    // Helper: radio group HTML
    function radioGroupHTML(name, options) {
        return '<div class="radio-group">' +
            options.map(([val, label]) =>
                '<label class="radio-option">' +
                '<input type="radio" name="' + name + '" value="' + val + '">' +
                '<span>' + label + '</span>' +
                '</label>'
            ).join('') +
        '</div>';
    }

    function getExtraFieldsHTML(prefix) {
        return `
            <!-- PLANO DE SAÚDE -->
            <div class="extra-fields" id="${prefix}fields-Saúde">
                <div class="form-group">
                    <p class="extra-fields-label">Escolha o tipo de plano</p>
                    ${radioGroupHTML(prefix + 'saudePlanType', [['Individual/Familiar','Plano Individual/Familiar'],['Empresarial','Plano Empresarial']])}
                </div>
                <div class="form-group" id="${prefix}saudeProfissaoGroup" style="display:none">
                    <input type="text" id="${prefix}saudeProfissao" placeholder="Profissão">
                </div>
                <div class="form-group">
                    <p class="extra-fields-label">Número de pessoas por faixa etária</p>
                    <div class="age-ranges-grid">${ageRangesHTML(prefix + 'saude')}</div>
                </div>
            </div>

            <!-- PLANO ODONTOLÓGICO -->
            <div class="extra-fields" id="${prefix}fields-Odontológico">
                <div class="form-group">
                    <p class="extra-fields-label">Escolha o tipo de plano</p>
                    ${radioGroupHTML(prefix + 'odontoPlanType', [['Individual/Familiar','Plano Individual/Familiar'],['Empresarial','Plano Empresarial']])}
                </div>
                <div class="form-group">
                    <p class="extra-fields-label">Número de pessoas por faixa etária</p>
                    <div class="age-ranges-grid">${ageRangesHTML(prefix + 'odonto')}</div>
                </div>
            </div>

            <!-- SEGURO AUTOMÓVEL -->
            <div class="extra-fields" id="${prefix}fields-Auto">
                <div class="form-group">
                    <input type="text" id="${prefix}autoMarca" placeholder="Marca (ex: Toyota)">
                </div>
                <div class="form-group">
                    <input type="text" id="${prefix}autoModelo" placeholder="Modelo (ex: Corolla)">
                </div>
                <div class="form-group">
                    <input type="text" id="${prefix}autoAno" placeholder="Ano (ex: 2022)">
                </div>
                <div class="form-group">
                    <select id="${prefix}autoUso">
                        <option value="" disabled selected>Uso do veículo</option>
                        <option value="Lazer/Trabalho">Lazer / Trabalho</option>
                        <option value="Aplicativo">Aplicativo (Uber, 99 etc.)</option>
                        <option value="Comercial">Comercial / Frota</option>
                    </select>
                </div>
                <div class="form-group">
                    <select id="${prefix}autoGaragem">
                        <option value="" disabled selected>Possui garagem?</option>
                        <option value="Sim">Sim</option>
                        <option value="Não">Não</option>
                    </select>
                </div>
                <div class="form-group">
                    <select id="${prefix}autoIdadeCondutor">
                        <option value="" disabled selected>Idade do condutor principal</option>
                        <option value="18-24">18 a 24 anos</option>
                        <option value="25-30">25 a 30 anos</option>
                        <option value="31-40">31 a 40 anos</option>
                        <option value="41-50">41 a 50 anos</option>
                        <option value="51+">Acima de 50 anos</option>
                    </select>
                </div>
            </div>

            <!-- CONSÓRCIO -->
            <div class="extra-fields" id="${prefix}fields-Consórcio">
                <div class="form-group">
                    <select id="${prefix}consorcioTipo">
                        <option value="" disabled selected>Tipo de consórcio</option>
                        <option value="Imóveis">Consórcio de Imóveis</option>
                        <option value="Automóveis">Consórcio de Automóveis</option>
                    </select>
                </div>
                <div class="form-group">
                    <input type="text" id="${prefix}consorcioCredito" placeholder="Valor do crédito desejado (R$)">
                </div>
                <div class="form-group">
                    <select id="${prefix}consorcioParcelas">
                        <option value="" disabled selected>Número de parcelas</option>
                        <option value="36">36 meses</option>
                        <option value="48">48 meses</option>
                        <option value="60">60 meses</option>
                        <option value="72">72 meses</option>
                        <option value="84">84 meses</option>
                        <option value="96">96 meses</option>
                        <option value="120">120 meses</option>
                    </select>
                </div>
            </div>

            <!-- SEGURO DE VIDA -->
            <div class="extra-fields" id="${prefix}fields-Vida">
                <div class="form-group">
                    <select id="${prefix}vidaSexo">
                        <option value="" disabled selected>Sexo</option>
                        <option value="Masculino">Masculino</option>
                        <option value="Feminino">Feminino</option>
                    </select>
                </div>
                <div class="form-group">
                    <input type="text" id="${prefix}vidaRenda" placeholder="Renda média (R$)">
                </div>
                <div class="form-group">
                    <p class="extra-fields-label">Fumante?</p>
                    ${radioGroupHTML(prefix + 'vidaFumante', [['Não','Não'],['Sim','Sim']])}
                </div>
                <div class="form-group">
                    <input type="text" id="${prefix}vidaCapital" placeholder="Capital segurado desejado (R$)">
                </div>
            </div>

            <!-- VIDA COLETIVO EMPRESARIAL -->
            <div class="extra-fields" id="${prefix}fields-VidaColetivo">
                <div class="form-group">
                    <select id="${prefix}vcSexo">
                        <option value="" disabled selected>Sexo predominante</option>
                        <option value="Masculino">Masculino</option>
                        <option value="Feminino">Feminino</option>
                        <option value="Misto">Misto</option>
                    </select>
                </div>
                <div class="form-group">
                    <input type="text" id="${prefix}vcRenda" placeholder="Renda média dos colaboradores (R$)">
                </div>
                <div class="form-group">
                    <p class="extra-fields-label">Fumante?</p>
                    ${radioGroupHTML(prefix + 'vcFumante', [['Não','Não'],['Sim','Sim']])}
                </div>
                <div class="form-group">
                    <input type="text" id="${prefix}vcCapitalSocio" placeholder="Capital por sócio/dirigente (R$)">
                </div>
                <div class="form-group">
                    <input type="text" id="${prefix}vcCapitalFunc" placeholder="Capital por funcionário (R$)">
                </div>
            </div>

            <!-- PREVIDÊNCIA PRIVADA -->
            <div class="extra-fields" id="${prefix}fields-Previdência">
                <div class="form-group">
                    <select id="${prefix}prevSexo">
                        <option value="" disabled selected>Sexo</option>
                        <option value="Masculino">Masculino</option>
                        <option value="Feminino">Feminino</option>
                    </select>
                </div>
                <div class="form-group">
                    <input type="text" id="${prefix}prevRenda" placeholder="Renda média (R$)">
                </div>
                <div class="form-group">
                    <p class="extra-fields-label">Fumante?</p>
                    ${radioGroupHTML(prefix + 'prevFumante', [['Não','Não'],['Sim','Sim']])}
                </div>
                <div class="form-group">
                    <input type="text" id="${prefix}prevAporte" placeholder="Aporte inicial (R$)">
                </div>
                <div class="form-group">
                    <input type="text" id="${prefix}prevContribuicao" placeholder="Contribuição mensal (R$)">
                </div>
            </div>

            <!-- SEGURO ESTAGIÁRIO -->
            <div class="extra-fields" id="${prefix}fields-Estagiário">
                <div class="form-group">
                    <input type="number" id="${prefix}estagiarioQtd" placeholder="Número de estagiários" min="1">
                </div>
                <div class="form-group">
                    <select id="${prefix}estagiarioSetor">
                        <option value="" disabled selected>Setor de atuação</option>
                        <option value="Administrativo">Administrativo</option>
                        <option value="Saúde">Saúde</option>
                        <option value="Educação">Educação</option>
                        <option value="Tecnologia">Tecnologia</option>
                        <option value="Engenharia">Engenharia</option>
                        <option value="Outro">Outro</option>
                    </select>
                </div>
            </div>

            <!-- PLANO DE SAÚDE PET -->
            <div class="extra-fields" id="${prefix}fields-Pet">
                <div class="form-group">
                    <select id="${prefix}petTipo">
                        <option value="" disabled selected>Tipo de pet</option>
                        <option value="Cão">Cão</option>
                        <option value="Gato">Gato</option>
                    </select>
                </div>
                <div class="form-group">
                    <input type="text" id="${prefix}petRaca" placeholder="Raça do pet">
                </div>
                <div class="form-group">
                    <select id="${prefix}petIdade">
                        <option value="" disabled selected>Idade do pet</option>
                        <option value="0-1 ano">0 a 1 ano</option>
                        <option value="1-3 anos">1 a 3 anos</option>
                        <option value="3-7 anos">3 a 7 anos</option>
                        <option value="7+ anos">Acima de 7 anos</option>
                    </select>
                </div>
            </div>

            <!-- SEGURO RESIDENCIAL -->
            <div class="extra-fields" id="${prefix}fields-Residencial">
                <div class="form-group">
                    <select id="${prefix}resImovelTipo">
                        <option value="" disabled selected>Tipo de imóvel</option>
                        <option value="Casa">Casa</option>
                        <option value="Apartamento">Apartamento</option>
                        <option value="Comercial">Comercial</option>
                    </select>
                </div>
                <div class="form-group">
                    <select id="${prefix}resOcupacao">
                        <option value="" disabled selected>Ocupação do imóvel</option>
                        <option value="Próprio habitado">Próprio habitado</option>
                        <option value="Alugado">Alugado</option>
                        <option value="Desocupado">Desocupado</option>
                    </select>
                </div>
                <div class="form-group">
                    <input type="text" id="${prefix}resValor" placeholder="Valor estimado do imóvel (R$)">
                </div>
            </div>

            <!-- SEGURO VIAGEM -->
            <div class="extra-fields" id="${prefix}fields-Viagem">
                <div class="form-group">
                    <select id="${prefix}viagemDestino">
                        <option value="" disabled selected>Destino</option>
                        <option value="Nacional">Nacional</option>
                        <option value="Internacional">Internacional</option>
                        <option value="Nacional e Internacional">Nacional e Internacional</option>
                    </select>
                </div>
                <div class="form-group extra-fields-label-wrap">
                    <label class="extra-fields-label" for="${prefix}viagemIda">Data de ida</label>
                    <input type="date" id="${prefix}viagemIda">
                </div>
                <div class="form-group extra-fields-label-wrap">
                    <label class="extra-fields-label" for="${prefix}viagemVolta">Data de volta</label>
                    <input type="date" id="${prefix}viagemVolta">
                </div>
                <div class="form-group">
                    <input type="number" id="${prefix}viagemViajantes" placeholder="Número de viajantes" min="1" value="1">
                </div>
            </div>

            <!-- SEGURO DE FROTAS -->
            <div class="extra-fields" id="${prefix}fields-Frotas">
                <div class="form-group">
                    <input type="number" id="${prefix}frotasQtd" placeholder="Número de veículos" min="2">
                </div>
                <div class="form-group">
                    <select id="${prefix}frotasTipo">
                        <option value="" disabled selected>Tipo de veículos</option>
                        <option value="Passeio">Passeio</option>
                        <option value="Utilitários">Utilitários</option>
                        <option value="Caminhões">Caminhões</option>
                        <option value="Misto">Misto</option>
                    </select>
                </div>
            </div>

            <!-- SEGURO DE CARGAS -->
            <div class="extra-fields" id="${prefix}fields-Cargas">
                <div class="form-group">
                    <select id="${prefix}cargasTipo">
                        <option value="" disabled selected>Tipo de carga</option>
                        <option value="Alimentos">Alimentos</option>
                        <option value="Eletrônicos">Eletrônicos</option>
                        <option value="Químicos">Químicos</option>
                        <option value="Geral">Geral</option>
                        <option value="Outro">Outro</option>
                    </select>
                </div>
                <div class="form-group">
                    <select id="${prefix}cargasTransporte">
                        <option value="" disabled selected>Modal de transporte</option>
                        <option value="Rodoviário">Rodoviário</option>
                        <option value="Aéreo">Aéreo</option>
                        <option value="Marítimo">Marítimo</option>
                        <option value="Multimodal">Multimodal</option>
                    </select>
                </div>
                <div class="form-group">
                    <input type="text" id="${prefix}cargasValor" placeholder="Valor médio da carga por viagem (R$)">
                </div>
            </div>

            <!-- SEGURO RESPONSABILIDADE CIVIL -->
            <div class="extra-fields" id="${prefix}fields-RC">
                <div class="form-group">
                    <select id="${prefix}rcAtividade">
                        <option value="" disabled selected>Atividade / Ramo</option>
                        <option value="Profissional Liberal">Profissional Liberal</option>
                        <option value="Médico / Saúde">Médico / Saúde</option>
                        <option value="Construtora / Obra">Construtora / Obra</option>
                        <option value="Prestador de Serviços">Prestador de Serviços</option>
                        <option value="Outro">Outro</option>
                    </select>
                </div>
                <div class="form-group">
                    <input type="text" id="${prefix}rcCapital" placeholder="Limite de cobertura desejado (R$)">
                </div>
            </div>

            <!-- SEGURO ACADEMIAS -->
            <div class="extra-fields" id="${prefix}fields-Academias">
                <div class="form-group">
                    <select id="${prefix}acadAtividade">
                        <option value="" disabled selected>Tipo de atividade</option>
                        <option value="Musculação / Crossfit">Musculação / Crossfit</option>
                        <option value="Artes Marciais">Artes Marciais</option>
                        <option value="Dança / Pilates">Dança / Pilates</option>
                        <option value="Esportes Coletivos">Esportes Coletivos</option>
                        <option value="Natação">Natação</option>
                        <option value="Outra">Outra</option>
                    </select>
                </div>
                <div class="form-group">
                    <input type="number" id="${prefix}acadAlunos" placeholder="Número de alunos / membros" min="1">
                </div>
                <div class="form-group">
                    <input type="text" id="${prefix}acadCapital" placeholder="Capital segurado desejado (R$)">
                </div>
            </div>
        `;
    }

    function extractExtraLeadData(prefix, product) {
        // Helper inline
        function val(id) { const el = document.getElementById(id); return el ? el.value.trim() : ''; }
        function radio(name) { const el = document.querySelector('input[name="' + name + '"]:checked'); return el ? el.value : ''; }
        function ageRangeData(pfx) {
            const sfxs = ['00_18','19_23','24_28','29_33','34_38','39_43','44_48','49_53','54_58','59_plus'];
            const out = {}; sfxs.forEach(s => { out[s] = +val(pfx + '_' + s); }); return out;
        }
        
        let leadData = {};
        switch (product) {
            case 'Saúde':
                leadData.plan_type      = radio(prefix + 'saudePlanType');
                leadData.profissao      = val(prefix + 'saudeProfissao');
                leadData.faixas_etarias = ageRangeData(prefix + 'saude');
                break;
            case 'Odontológico':
                leadData.plan_type      = radio(prefix + 'odontoPlanType');
                leadData.faixas_etarias = ageRangeData(prefix + 'odonto');
                break;
            case 'Auto':
                leadData.marca           = val(prefix + 'autoMarca');
                leadData.modelo          = val(prefix + 'autoModelo');
                leadData.ano             = val(prefix + 'autoAno');
                leadData.uso             = val(prefix + 'autoUso');
                leadData.garagem         = val(prefix + 'autoGaragem');
                leadData.idade_condutor  = val(prefix + 'autoIdadeCondutor');
                break;
            case 'Consórcio':
                leadData.tipo_consorcio = val(prefix + 'consorcioTipo');
                leadData.credito        = val(prefix + 'consorcioCredito');
                leadData.parcelas       = val(prefix + 'consorcioParcelas');
                break;
            case 'Vida':
                leadData.sexo    = val(prefix + 'vidaSexo');
                leadData.renda   = val(prefix + 'vidaRenda');
                leadData.fumante = radio(prefix + 'vidaFumante');
                leadData.capital = val(prefix + 'vidaCapital');
                break;
            case 'VidaColetivo':
                leadData.sexo              = val(prefix + 'vcSexo');
                leadData.renda             = val(prefix + 'vcRenda');
                leadData.fumante           = radio(prefix + 'vcFumante');
                leadData.capital_socio     = val(prefix + 'vcCapitalSocio');
                leadData.capital_funcionario = val(prefix + 'vcCapitalFunc');
                break;
            case 'Previdência':
                leadData.sexo         = val(prefix + 'prevSexo');
                leadData.renda        = val(prefix + 'prevRenda');
                leadData.fumante      = radio(prefix + 'prevFumante');
                leadData.aporte       = val(prefix + 'prevAporte');
                leadData.contribuicao = val(prefix + 'prevContribuicao');
                break;
            case 'Estagiário':
                leadData.qtd_estagiarios = val(prefix + 'estagiarioQtd');
                leadData.setor           = val(prefix + 'estagiarioSetor');
                break;
            case 'Pet':
                leadData.tipo_pet  = val(prefix + 'petTipo');
                leadData.raca      = val(prefix + 'petRaca');
                leadData.idade_pet = val(prefix + 'petIdade');
                break;
            case 'Residencial':
                leadData.tipo_imovel = val(prefix + 'resImovelTipo');
                leadData.ocupacao    = val(prefix + 'resOcupacao');
                leadData.valor       = val(prefix + 'resValor');
                break;
            case 'Viagem':
                leadData.destino    = val(prefix + 'viagemDestino');
                leadData.data_ida   = val(prefix + 'viagemIda');
                leadData.data_volta = val(prefix + 'viagemVolta');
                leadData.viajantes  = val(prefix + 'viagemViajantes');
                break;
            case 'Frotas':
                leadData.qtd_veiculos  = val(prefix + 'frotasQtd');
                leadData.tipo_veiculos = val(prefix + 'frotasTipo');
                break;
            case 'Cargas':
                leadData.tipo_carga = val(prefix + 'cargasTipo');
                leadData.transporte = val(prefix + 'cargasTransporte');
                leadData.valor      = val(prefix + 'cargasValor');
                break;
            case 'RC':
                leadData.atividade = val(prefix + 'rcAtividade');
                leadData.capital   = val(prefix + 'rcCapital');
                break;
            case 'Academias':
                leadData.atividade = val(prefix + 'acadAtividade');
                leadData.alunos    = val(prefix + 'acadAlunos');
                leadData.capital   = val(prefix + 'acadCapital');
                break;
        }
        return leadData;
    }

    // Attach listeners function
    function setupExtraFieldsListeners(prefix) {
        document.querySelectorAll('input[name="'+prefix+'saudePlanType"]').forEach(radio => {
            radio.addEventListener('change', () => {
                const checked = document.querySelector('input[name="'+prefix+'saudePlanType"]:checked');
                const group = document.getElementById(prefix+'saudeProfissaoGroup');
                if (group) {
                    group.style.display = (checked && checked.value === 'Individual/Familiar') ? 'block' : 'none';
                }
            });
        });
    }



    // ===========================
    // QUOTE MODAL & PIPEDRIVE INTEGRATION
    // ===========================
    function initQuoteModal() {

                // 1. Inject Modal HTML
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
                            <input type="tel" id="modalPhone" placeholder="Seu telefone / WhatsApp" required>
                        </div>
                        <div class="form-group">
                            <input type="email" id="modalEmail" placeholder="Seu e-mail">
                        </div>
                        <div class="form-group">
                            <select id="modalProduct" required>
                                <option value="" disabled selected>Selecione seu produto</option>
                                <option value="Saúde">Plano de Saúde</option>
                                <option value="Odontológico">Plano Odontológico</option>
                                <option value="Auto">Seguro Automóvel</option>
                                <option value="Consórcio">Consórcio de Imóveis e Automóveis</option>
                                <option value="Vida">Seguro de Vida</option>
                                <option value="VidaColetivo">Seguro de Vida Coletivo Empresarial</option>
                                <option value="Previdência">Previdência Privada</option>
                                <option value="Estagiário">Seguro Estagiário</option>
                                <option value="Pet">Plano de Saúde Pet</option>
                                <option value="Residencial">Seguro Residencial</option>
                                <option value="Viagem">Seguro Viagem</option>
                                <option value="Frotas">Seguro de Frotas</option>
                                <option value="Cargas">Seguro de Cargas</option>
                                <option value="RC">Seguro Responsabilidade Civil</option>
                                <option value="Academias">Seguro Academias</option>
                            </select>
                        </div>

                        ${getExtraFieldsHTML('modal_')}

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
        const productSelect = document.getElementById('modalProduct');
        
        // Show extra fields section for the selected product
        function showExtraFields(product) {
            modalForm.querySelectorAll('.extra-fields').forEach(el => el.classList.remove('visible'));
            if (product) {
                const target = document.getElementById('modal_fields-' + product);
                if (target) target.classList.add('visible');
            }
            setupExtraFieldsListeners('modal_');
        }

        productSelect.addEventListener('change', () => showExtraFields(productSelect.value));

        // 2. Open Modal Logic
        function openModal(e) {
            e.preventDefault();
            overlay.classList.add('active');
            document.body.style.overflow = 'hidden';

            // Pre-select product based on page title
            const t = document.title.toLowerCase();
            let product = '';
            if      (t.includes('pet'))                                      product = 'Pet';
            else if (t.includes('saúde') || t.includes('saude'))             product = 'Saúde';
            else if (t.includes('odonto'))                                   product = 'Odontológico';
            else if (t.includes('automóvel') || t.includes('auto'))          product = 'Auto';
            else if (t.includes('consórcio') || t.includes('consorcio'))     product = 'Consórcio';
            else if (t.includes('coletivo'))                                 product = 'VidaColetivo';
            else if (t.includes('vida'))                                     product = 'Vida';
            else if (t.includes('previdência') || t.includes('previdencia')) product = 'Previdência';
            else if (t.includes('estagiário') || t.includes('estagiario'))   product = 'Estagiário';
            else if (t.includes('residencial'))                              product = 'Residencial';
            else if (t.includes('viagem'))                                   product = 'Viagem';
            else if (t.includes('frota'))                                    product = 'Frotas';
            else if (t.includes('carga'))                                    product = 'Cargas';
            else if (t.includes('responsabilidade'))                         product = 'RC';
            else if (t.includes('academia'))                                 product = 'Academias';

            if (product) productSelect.value = product;
            showExtraFields(productSelect.value);
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

        document.querySelectorAll('.open-quote-modal').forEach(btn => {
            btn.addEventListener('click', openModal);
        });

        

        // 4. Form Submission → Pipedrive via Webhook
        modalForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const submitBtn = modalForm.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = 'Enviando...';
            submitBtn.disabled = true;

            const product = productSelect.value;
            function val(id) { const el = document.getElementById(id); return el ? el.value.trim() : ''; }

            const leadData = {
                name: val('modalName'),
                phone: val('modalPhone'),
                email: val('modalEmail'),
                product,
                message: val('modalMessage'),
                source: 'Site Virtua Corretora',
                page_url: window.location.href,
                page_title: document.title,
                submitted_at: new Date().toISOString()
            };

            // Extract extra fields
            Object.assign(leadData, extractExtraLeadData('modal_', product));

            try {
                const response = await fetch(WEBHOOK_URL, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(leadData)
                });
                if (!response.ok) throw new Error('HTTP ' + response.status);
            } catch (error) {
                console.error('Erro ao enviar lead:', error);
                submitBtn.innerHTML = '⚠️ Tente novamente';
                submitBtn.style.background = '#ef4444';
                submitBtn.disabled = false;
                setTimeout(() => {
                    submitBtn.innerHTML = originalText;
                    submitBtn.style.background = '';
                }, 3000);
                return;
            }

            submitBtn.innerHTML = '✅ Recebemos seu pedido!';
            submitBtn.style.background = 'var(--green)';
            submitBtn.style.boxShadow = '0 4px 15px rgba(16, 185, 129, 0.35)';

            setTimeout(() => {
                closeModal();
                setTimeout(() => {
                    submitBtn.innerHTML = originalText;
                    submitBtn.style.background = '';
                    submitBtn.style.boxShadow = '';
                    submitBtn.disabled = false;
                    modalForm.reset();
                    showExtraFields(null);
                    const pG = document.getElementById('modal_saudeProfissaoGroup'); if(pG) pG.style.display = 'none';
                }, 300);
            }, 2000);
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

    // ===========================
    // WHATSAPP LEAD MODAL
    // ===========================
    function initWhatsAppModal() {
        const modalHTML = `
            <div class="quote-modal-overlay" id="waModalOverlay">
                <div class="quote-modal" style="max-width: 400px; text-align: center;">
                    <button class="quote-modal-close" id="waModalClose" aria-label="Fechar">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="18" y1="6" x2="6" y2="18"></line>
                            <line x1="6" y1="6" x2="18" y2="18"></line>
                        </svg>
                    </button>
                    <div class="quote-modal-header" style="margin-bottom: 20px;">
                        <h2 class="quote-modal-title" style="font-size: 22px;">Qual sua necessidade hoje?</h2>
                        <p class="quote-modal-desc">Faça uma Simulação pelo <span style="color:var(--primary); font-weight:700;">WhatsApp</span></p>
                    </div>
                    <form class="quote-modal-form" id="waModalForm">
                        <div class="form-group">
                            <input type="text" id="waName" placeholder="Seu nome" required>
                        </div>
                        <div class="form-group">
                            <input type="tel" id="waPhone" placeholder="Seu número de WhatsApp" required>
                        </div>
                        <div class="form-group">
                            <input type="email" id="waEmail" placeholder="Seu email">
                        </div>
                        <div class="form-group">
                            <input type="text" id="waCity" placeholder="Cidade">
                        </div>
                        <div class="form-group">
                            <select id="waProduct" required>
                                <option value="" disabled selected>Selecione seu produto</option>
                                <option value="Plano de Saúde">Plano de Saúde</option>
                                <option value="Plano Odontológico">Plano Odontológico</option>
                                <option value="Seguro Automóvel">Seguro Automóvel</option>
                                <option value="Seguro de Vida">Seguro de Vida</option>
                                <option value="Consórcio">Consórcio</option>
                                <option value="Previdência Privada">Previdência Privada</option>
                                <option value="Seguro Residencial">Seguro Residencial</option>
                                <option value="Seguro Empresarial">Seguro Empresarial</option>
                                <option value="Outros">Outros</option>
                            </select>
                        </div>
                        <button type="submit" class="btn btn-primary btn-lg" style="width:100%; background:#25D366; border-color:#25D366; display:flex; align-items:center; justify-content:center; gap:8px;">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                            WHATSAPP
                        </button>
                    </form>
                </div>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', modalHTML);

        const overlay = document.getElementById('waModalOverlay');
        const btnClose = document.getElementById('waModalClose');
        const form = document.getElementById('waModalForm');
        let currentWaUrl = 'https://wa.me/5522999404840';

        function openModal(e) {
            e.preventDefault();
            // Get closest link in case inner icon is clicked
            const link = e.currentTarget;
            currentWaUrl = link.href;

            // Pre-select product based on page content if possible, or just reset
            overlay.classList.add('active');
            document.body.style.overflow = 'hidden';
            
            // Try pre-fill product from title
            const t = document.title.toLowerCase();
            const productSelect = document.getElementById('waProduct');
            let product = '';
            if (t.includes('saúde') || t.includes('saude')) product = 'Plano de Saúde';
            else if (t.includes('odonto')) product = 'Plano Odontológico';
            else if (t.includes('auto')) product = 'Seguro Automóvel';
            else if (t.includes('vida')) product = 'Seguro de Vida';
            else if (t.includes('consórcio') || t.includes('consorcio')) product = 'Consórcio';
            else if (t.includes('previdência')) product = 'Previdência Privada';
            else if (t.includes('residencial')) product = 'Seguro Residencial';

            if (product) {
                // Check if option exists and set it
                const opts = Array.from(productSelect.options);
                const opt = opts.find(o => o.value === product);
                if (opt) productSelect.value = product;
            }
        }

        function closeModal() {
            overlay.classList.remove('active');
            document.body.style.overflow = '';
        }

        if (btnClose) btnClose.addEventListener('click', closeModal);
        if (overlay) overlay.addEventListener('click', (e) => {
            if (e.target === overlay) closeModal();
        });

        // Intercept all whatsapp links
        document.querySelectorAll('a[href*="wa.me"], a[href*="api.whatsapp.com/send"]').forEach(link => {
            // Se já tem .open-contact-modal (que é o modal de vários contatos), deixa como está
            if(!link.classList.contains('open-contact-modal')) {
                link.addEventListener('click', openModal);
            }
        });

        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = form.querySelector('button[type="submit"]');
            const originalText = btn.innerHTML;
            btn.innerHTML = 'Redirecionando...';

            const name = document.getElementById('waName').value.trim();
            const phone = document.getElementById('waPhone').value.trim();
            const email = document.getElementById('waEmail').value.trim();
            const city = document.getElementById('waCity').value.trim();
            const product = document.getElementById('waProduct').value;

            // Extract phone from current URL
            let targetPhone = '5522999404840'; // fallback
            let originalTextParam = '';

            try {
                const urlObj = new URL(currentWaUrl);
                if (currentWaUrl.includes('wa.me')) {
                    targetPhone = urlObj.pathname.replace('/', '') || targetPhone;
                    originalTextParam = urlObj.searchParams.get('text') || '';
                } else if (currentWaUrl.includes('whatsapp.com')) {
                    targetPhone = urlObj.searchParams.get('phone') || targetPhone;
                    originalTextParam = urlObj.searchParams.get('text') || '';
                }
            } catch (err) {}

            // Build WhatsApp message
            let msg = `Olá, meu nome é ${name} e gostaria de saber mais informações sobre ${product}.`;
            if (email) msg += ` Email: ${email}.`;
            if (city) msg += ` Cidade: ${city}.`;
            // Include original context if any
            if (originalTextParam) {
                msg += `\n\n(Contexto: ${originalTextParam})`;
            }

            // Webhook send (optional/background)
            const leadData = {
                name, phone, email, city, product,
                source: 'WhatsApp Modal',
                page_url: window.location.href,
                page_title: document.title,
                submitted_at: new Date().toISOString()
            };

            try {
                // Enviar pro webhook do Pipedrive via fetch de background (nao esperamos terminar pra nao atrasar o usuario)
                fetch(WEBHOOK_URL, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(leadData)
                }).catch(e=>console.log(e));
            } catch (err) {}

            const finalUrl = `https://api.whatsapp.com/send/?phone=${targetPhone}&text=${encodeURIComponent(msg)}`;
            
            setTimeout(() => {
                btn.innerHTML = originalText;
                closeModal();
                form.reset();
                window.open(finalUrl, '_blank');
            }, 600);
        });
    }

    initQuoteModal();
    initContactModal();
    initWhatsAppModal();
});
