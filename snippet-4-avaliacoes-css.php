<?php
/**
 * Snippet: CSS para Seção "Como somos avaliados" com Google e Reclame Aqui
 * Descrição: Estiliza a seção de avaliações com cards bonitos
 * Onde executar: Somente no front-end
 * 
 * INSTRUÇÕES:
 * 1. WP Admin → Snippets → Adicionar Novo
 * 2. Nome: "CSS - Seção Avaliações"
 * 3. Cole este código
 * 4. Em "Executar apenas": selecione "Somente no front-end"  
 * 5. Salvar e Ativar
 * 
 * NOTA: Este snippet injeta o CSS. O HTML será adicionado via Elementor (widget HTML).
 */

add_action('wp_head', function () {
    ?>
    <style>
        /* === Seção Como somos avaliados === */
        .virtua-avaliacoes-container {
            display: flex;
            gap: 40px;
            justify-content: center;
            align-items: stretch;
            flex-wrap: wrap;
            padding: 20px 0;
            max-width: 900px;
            margin: 0 auto;
        }

        .virtua-avaliacao-card {
            background: #ffffff;
            border-radius: 16px;
            padding: 40px 35px;
            text-align: center;
            flex: 1;
            min-width: 280px;
            max-width: 400px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border: 1px solid rgba(0, 0, 0, 0.05);
        }

        .virtua-avaliacao-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
        }

        .virtua-avaliacao-logo {
            height: 45px;
            margin-bottom: 20px;
            object-fit: contain;
        }

        .virtua-avaliacao-nota {
            font-size: 48px;
            font-weight: 800;
            line-height: 1;
            margin-bottom: 8px;
        }

        .virtua-avaliacao-nota.google {
            color: #1a73e8;
        }

        .virtua-avaliacao-nota.reclameaqui {
            color: #00b67a;
        }

        .virtua-avaliacao-estrelas {
            color: #fbbc04;
            font-size: 22px;
            margin-bottom: 12px;
            letter-spacing: 2px;
        }

        .virtua-avaliacao-texto {
            font-size: 14px;
            color: #666;
            margin: 0;
            line-height: 1.5;
        }

        .virtua-avaliacao-badge {
            display: inline-block;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            margin-top: 15px;
        }

        .virtua-avaliacao-badge.google {
            background: #e8f0fe;
            color: #1a73e8;
        }

        .virtua-avaliacao-badge.reclameaqui {
            background: #e6f9f1;
            color: #00b67a;
        }

        /* Responsivo */
        @media (max-width: 768px) {
            .virtua-avaliacoes-container {
                flex-direction: column;
                align-items: center;
                gap: 20px;
            }

            .virtua-avaliacao-card {
                width: 100%;
                max-width: 350px;
            }

            .virtua-avaliacao-nota {
                font-size: 40px;
            }
        }
    </style>
    <?php
});
