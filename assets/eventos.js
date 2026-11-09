/**
 * assets/eventos.js
 *
 * Purpose: anonymous counting of the guide site: one page view per page and the clicks marked with
 *          data-ev="..." (download the guide, WhatsApp), plus the events the pages call by hand
 *          through window.ev(). Sends a text/plain beacon to absoluto.ai/api/evento: no cookie, no
 *          id, nothing about the visitor except the campaign source of the link they came from
 *          (utm_source/utm_campaign, kept in sessionStorage so the preparer page still knows it).
 * Exports: window.ev(nome) → void.
 * Shared:  index.html and preparar.html; server side in site/src/app/api/evento/route.ts (fixed list
 *          of event names there); report in linkedin/automacao/guia-analytics/relatorio.sh.
 * Perf:    loaded with defer; sendBeacon does not block navigation or the download.
 */
(() => {
  const DESTINO = 'https://absoluto.ai/api/evento';
  const BASE = '/time-de-seo-geo';
  let origem = { us: '', uc: '' };
  try {
    const q = new URLSearchParams(location.search);
    if (q.get('utm_source')) {
      origem = { us: q.get('utm_source'), uc: q.get('utm_campaign') || '' };
      sessionStorage.setItem('guia-origem', JSON.stringify(origem));
    } else {
      origem = JSON.parse(sessionStorage.getItem('guia-origem') || 'null') || origem;
    }
  } catch { /* storage blocked: count without the source */ }
  let ref = '';
  try { ref = document.referrer ? new URL(document.referrer).hostname : ''; } catch { /* no referrer */ }
  const pagina = (location.pathname.startsWith(BASE) ? location.pathname.slice(BASE.length) : location.pathname) || '/';

  function ev(nome) {
    try {
      const body = JSON.stringify({ e: nome, p: pagina, r: ref, us: origem.us, uc: origem.uc });
      if (navigator.sendBeacon) navigator.sendBeacon(DESTINO, new Blob([body], { type: 'text/plain' }));
      else fetch(DESTINO, { method: 'POST', body, keepalive: true, mode: 'no-cors' });
    } catch { /* counting never breaks the page */ }
  }

  window.ev = ev;
  ev('pageview');
  document.addEventListener('click', (event) => {
    const alvo = event.target.closest && event.target.closest('[data-ev]');
    if (alvo) ev(alvo.dataset.ev);
  });
})();
