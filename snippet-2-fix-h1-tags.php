<?php
/**
 * Snippet: Corrigir H1 Duplicados - Slides do Carrossel (v2)
 * Descrição: Converte H1 extras dos slides em H2, mantendo apenas 1 H1 na página
 * Inclui MutationObserver para capturar H1 criados dinamicamente pelo carrossel
 * Onde executar: Somente no front-end
 */

add_action('wp_footer', function () {
    if (is_front_page() || is_home()) {
        ?>
        <script>
            (function () {
                'use strict';

                function convertH1toH2(h1) {
                    var h2 = document.createElement('h2');
                    h2.innerHTML = h1.innerHTML;
                    h2.className = h1.className;
                    if (h1.id) h2.id = h1.id;
                    if (h1.style.cssText) h2.style.cssText = h1.style.cssText;
                    var computed = window.getComputedStyle(h1);
                    h2.style.fontSize = computed.fontSize;
                    h2.style.fontWeight = computed.fontWeight;
                    h2.style.fontFamily = computed.fontFamily;
                    h2.style.color = computed.color;
                    h2.style.lineHeight = computed.lineHeight;
                    h2.style.letterSpacing = computed.letterSpacing;
                    h2.style.textTransform = computed.textTransform;
                    h2.style.margin = computed.margin;
                    h2.style.padding = computed.padding;
                    h1.parentNode.replaceChild(h2, h1);
                }

                function fixH1Tags() {
                    var allH1 = document.querySelectorAll('h1');
                    if (allH1.length > 1) {
                        var count = 0;
                        for (var i = 1; i < allH1.length; i++) {
                            convertH1toH2(allH1[i]);
                            count++;
                        }
                        console.log('[Virtua SEO] H1 corrigidos: ' + count + ' convertido(s). Total H1: ' + document.querySelectorAll('h1').length);
                    }
                }

                // Executa inicialmente
                if (document.readyState === 'loading') {
                    document.addEventListener('DOMContentLoaded', fixH1Tags);
                } else {
                    fixH1Tags();
                }

                // Observa novos H1 criados dinamicamente (carrossel Elementor clona slides)
                var observer = new MutationObserver(function () {
                    var allH1 = document.querySelectorAll('h1');
                    if (allH1.length > 1) {
                        for (var i = 1; i < allH1.length; i++) {
                            convertH1toH2(allH1[i]);
                        }
                    }
                });

                if (document.body) {
                    observer.observe(document.body, { childList: true, subtree: true });
                } else {
                    document.addEventListener('DOMContentLoaded', function () {
                        observer.observe(document.body, { childList: true, subtree: true });
                    });
                }

                // Fallback: re-checa apos 2s e 5s (carrosseis com delay)
                setTimeout(fixH1Tags, 2000);
                setTimeout(fixH1Tags, 5000);
            })();
        </script>
        <?php
    }
});
