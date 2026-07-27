import json, base64, os

OUT = "/sessions/pensive-relaxed-darwin/mnt/outputs"
REPO = "/sessions/pensive-relaxed-darwin/mnt/youcord"

plugins = json.load(open(f"{OUT}/_plugins_slim.json", encoding="utf-8"))
icon_b64 = base64.b64encode(open(f"{REPO}/icon.png","rb").read()).decode()

DOWNLOAD_URL = "https://github.com/nightcordlegit/youcord/releases/latest/download/YouCord-Setup.exe"
RELEASES_URL = "https://github.com/nightcordlegit/youcord/releases/latest"
GITHUB_URL   = "https://github.com/nightcordlegit/youcord"
TELEGRAM_URL = "https://t.me/youcordoff"
SITE_URL     = "https://youcord.fr"
VERSION      = "1.21.30"

HTML = r"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>YouCord — Le client Discord rapide et open source</title>
<meta name="description" content="YouCord : un client Discord personnalisé, rapide et sans bloat. Fork propre d'Equicord/Vencord avec 380 plugins. Téléchargez le .exe pour Windows ou le .dmg pour Mac.">
<link rel="icon" href="data:image/png;base64,__ICON_B64__">
<style>
:root{
  --purple:#8b2ff0; --purple-2:#a848f0; --purple-deep:#6018d8; --purple-dark:#300078;
  --gold:#ffc800; --gold-2:#ffd500; --gold-deep:#f0a800;
  --bg:#0c0716; --bg-2:#120a24; --card:#191033; --card-2:#1f1440;
  --line:#2c1f52; --txt:#f0eefb; --muted:#a99fca; --white:#f0f0f0;
  --radius:16px; --maxw:1160px;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{
  font-family:'Segoe UI',system-ui,-apple-system,Roboto,Helvetica,Arial,sans-serif;
  background:var(--bg); color:var(--txt); line-height:1.6;
  -webkit-font-smoothing:antialiased; overflow-x:hidden;
}
a{color:inherit;text-decoration:none}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 22px}
.grad-text{background:linear-gradient(120deg,var(--gold) 0%,var(--gold-2) 30%,var(--purple-2) 70%,var(--purple) 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}

/* ---------- NAV ---------- */
header.nav{position:sticky;top:0;z-index:50;backdrop-filter:blur(14px);background:rgba(12,7,22,.72);border-bottom:1px solid var(--line)}
.nav-in{display:flex;align-items:center;gap:18px;height:64px}
.brand{display:flex;align-items:center;gap:10px;font-weight:800;font-size:19px}
.brand img{width:34px;height:34px;filter:drop-shadow(0 2px 8px rgba(139,47,240,.5))}
.nav-links{display:flex;gap:26px;margin-left:14px}
.nav-links a{color:var(--muted);font-size:15px;font-weight:500;transition:.2s}
.nav-links a:hover{color:var(--white)}
.nav-cta{margin-left:auto;display:flex;gap:10px;align-items:center}
.btn{display:inline-flex;align-items:center;gap:9px;border-radius:12px;padding:11px 20px;font-weight:700;font-size:15px;cursor:pointer;border:1px solid transparent;transition:transform .15s ease,box-shadow .2s ease,background .2s}
.btn:hover{transform:translateY(-2px)}
.btn-gold{background:linear-gradient(120deg,var(--gold-deep),var(--gold-2));color:#231000;box-shadow:0 8px 24px rgba(255,200,0,.28)}
.btn-gold:hover{box-shadow:0 12px 30px rgba(255,200,0,.42)}
.btn-purple{background:linear-gradient(120deg,var(--purple-deep),var(--purple-2));color:#fff;box-shadow:0 8px 24px rgba(139,47,240,.35)}
.btn-ghost{background:rgba(255,255,255,.04);border-color:var(--line);color:var(--txt)}
.btn-ghost:hover{background:rgba(255,255,255,.08)}
.nav-burger{display:none;margin-left:auto;background:none;border:0;color:#fff;font-size:26px;cursor:pointer}

/* ---------- HERO ---------- */
.hero{position:relative;padding:78px 0 60px;text-align:center;overflow:hidden}
.hero::before{content:"";position:absolute;inset:0;background:
  radial-gradient(700px 380px at 50% -60px,rgba(139,47,240,.42),transparent 65%),
  radial-gradient(560px 300px at 82% 8%,rgba(255,200,0,.14),transparent 60%),
  radial-gradient(520px 300px at 15% 20%,rgba(96,24,216,.30),transparent 60%);
  z-index:-1}
.hero-logo{width:120px;height:120px;margin:0 auto 22px;filter:drop-shadow(0 10px 34px rgba(139,47,240,.6));animation:float 5s ease-in-out infinite}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}
.hero h1{font-size:clamp(46px,8vw,84px);line-height:1;font-weight:900;letter-spacing:-2px}
.hero .tag{font-size:clamp(17px,2.6vw,22px);color:var(--txt);margin-top:18px;font-weight:600}
.hero .sub{max-width:620px;margin:14px auto 0;color:var(--muted);font-size:16px}
.hero-btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:34px}
.hero-btns .btn{padding:15px 28px;font-size:16px}
.meta-row{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:22px}
.pill{display:inline-flex;align-items:center;gap:7px;font-size:13px;color:var(--muted);background:rgba(255,255,255,.04);border:1px solid var(--line);padding:6px 13px;border-radius:999px}
.pill b{color:var(--white)}
.dot{width:8px;height:8px;border-radius:50%;background:var(--gold)}
.dot.g{background:#22c55e}

/* ---------- TRUST ---------- */
.trust{max-width:760px;margin:30px auto 0;display:flex;gap:12px;align-items:flex-start;background:rgba(34,197,94,.07);border:1px solid rgba(34,197,94,.28);border-radius:14px;padding:15px 18px;text-align:left}
.trust .ic{font-size:20px;line-height:1.3}
.trust p{font-size:14px;color:#cfeede}
.trust b{color:#fff}

/* ---------- STATS ---------- */
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin:56px 0 8px}
.stat{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:22px;text-align:center}
.stat .num{font-size:40px;font-weight:900;line-height:1}
.stat .lbl{color:var(--muted);font-size:14px;margin-top:6px}

/* ---------- SECTIONS ---------- */
section{padding:64px 0}
.sec-head{text-align:center;max-width:640px;margin:0 auto 42px}
.sec-head .kicker{color:var(--gold);font-weight:800;letter-spacing:2px;font-size:13px;text-transform:uppercase}
.sec-head h2{font-size:clamp(30px,5vw,44px);font-weight:900;margin-top:8px;letter-spacing:-1px}
.sec-head p{color:var(--muted);margin-top:12px;font-size:16px}

/* ---------- FEATURES ---------- */
.feat-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.feat{background:linear-gradient(180deg,var(--card),var(--bg-2));border:1px solid var(--line);border-radius:var(--radius);padding:26px;transition:.25s}
.feat:hover{transform:translateY(-4px);border-color:var(--purple-2);box-shadow:0 16px 40px rgba(139,47,240,.18)}
.feat .fic{width:52px;height:52px;display:grid;place-items:center;border-radius:13px;font-size:26px;background:linear-gradient(135deg,rgba(139,47,240,.25),rgba(255,200,0,.18));border:1px solid var(--line);margin-bottom:16px}
.feat h3{font-size:19px;font-weight:800}
.feat p{color:var(--muted);font-size:15px;margin-top:8px}

/* ---------- PLUGINS ---------- */
.plug-controls{display:flex;flex-direction:column;gap:16px;margin-bottom:26px}
.search-box{position:relative;max-width:520px;margin:0 auto;width:100%}
.search-box input{width:100%;background:var(--card);border:1px solid var(--line);color:var(--txt);border-radius:12px;padding:14px 16px 14px 44px;font-size:15px;outline:none;transition:.2s}
.search-box input:focus{border-color:var(--purple-2);box-shadow:0 0 0 3px rgba(139,47,240,.22)}
.search-box .si{position:absolute;left:15px;top:50%;transform:translateY(-50%);opacity:.6}
.chips{display:flex;gap:8px;flex-wrap:wrap;justify-content:center}
.chip{cursor:pointer;font-size:13px;font-weight:600;color:var(--muted);background:var(--card);border:1px solid var(--line);padding:7px 14px;border-radius:999px;transition:.18s;user-select:none}
.chip:hover{color:var(--white);border-color:var(--purple-2)}
.chip.active{background:linear-gradient(120deg,var(--purple-deep),var(--purple-2));color:#fff;border-color:transparent}
.chip.yc.active{background:linear-gradient(120deg,var(--gold-deep),var(--gold-2));color:#231000}
.count-row{text-align:center;color:var(--muted);font-size:14px;margin-bottom:18px}
.count-row b{color:var(--gold)}
.plug-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px}
.pcard{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 17px;transition:.18s;display:flex;flex-direction:column;gap:8px}
.pcard:hover{transform:translateY(-3px);border-color:var(--purple-2);box-shadow:0 12px 28px rgba(0,0,0,.35)}
.pcard-top{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.pcard h4{font-size:16px;font-weight:800}
.badge{font-size:10.5px;font-weight:800;letter-spacing:.4px;padding:2px 8px;border-radius:999px;text-transform:uppercase}
.badge.yc{background:linear-gradient(120deg,var(--gold-deep),var(--gold-2));color:#231000}
.badge.core{background:rgba(139,47,240,.2);color:#c9a6ff;border:1px solid var(--purple-2)}
.badge.on{background:rgba(34,197,94,.16);color:#7ee2a4;border:1px solid rgba(34,197,94,.4)}
.pcard p{color:var(--muted);font-size:13.5px;flex:1}
.ptags{display:flex;gap:6px;flex-wrap:wrap;margin-top:2px}
.ptag{font-size:11px;color:#bfb3e6;background:rgba(139,47,240,.12);border:1px solid var(--line);padding:2px 8px;border-radius:6px}
.pauth{font-size:12px;color:#7c729a}
.no-res{text-align:center;color:var(--muted);padding:40px;grid-column:1/-1}
.load-more{display:block;margin:26px auto 0}

/* ---------- INSTALL ---------- */
.install-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:22px}
.icard{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:26px}
.icard h3{font-size:20px;font-weight:800;display:flex;align-items:center;gap:10px}
.icard .step{color:var(--muted);font-size:15px;margin:14px 0;display:flex;gap:12px}
.icard .step .n{flex:none;width:26px;height:26px;border-radius:50%;background:linear-gradient(135deg,var(--purple-deep),var(--purple-2));color:#fff;font-weight:800;font-size:13px;display:grid;place-items:center}
.code{background:#0a0614;border:1px solid var(--line);border-radius:10px;padding:13px 15px;font-family:'Consolas','Courier New',monospace;font-size:13.5px;color:#e7d9ff;overflow-x:auto;position:relative;margin-top:6px}
.copy{position:absolute;top:8px;right:8px;background:rgba(255,255,255,.06);border:1px solid var(--line);color:var(--muted);border-radius:7px;padding:4px 10px;font-size:12px;cursor:pointer}
.copy:hover{color:#fff}
.tiny{font-size:12.5px;color:#7c729a;margin-top:12px}

/* ---------- FOOTER ---------- */
footer{border-top:1px solid var(--line);background:var(--bg-2);padding:48px 0 30px;margin-top:30px}
.foot-grid{display:flex;justify-content:space-between;gap:30px;flex-wrap:wrap}
.foot-brand{max-width:340px}
.foot-brand .brand{margin-bottom:12px}
.foot-brand p{color:var(--muted);font-size:14px}
.foot-links{display:flex;gap:56px;flex-wrap:wrap}
.foot-col h5{font-size:13px;text-transform:uppercase;letter-spacing:1px;color:var(--muted);margin-bottom:12px}
.foot-col a{display:block;color:var(--txt);font-size:14.5px;margin-bottom:9px;transition:.15s}
.foot-col a:hover{color:var(--gold)}
.disc{margin-top:34px;padding-top:20px;border-top:1px solid var(--line);color:#6d6488;font-size:12.5px;text-align:center;line-height:1.7}

@media(max-width:900px){
  .stats{grid-template-columns:repeat(2,1fr)}
  .feat-grid{grid-template-columns:1fr}
  .install-grid{grid-template-columns:1fr}
  .nav-links{display:none}
}
@media(max-width:620px){
  .nav-cta .btn span.lbl{display:none}
}
</style>
</head>
<body>

<header class="nav">
  <div class="wrap nav-in">
    <a class="brand" href="#top"><img src="data:image/png;base64,__ICON_B64__" alt="YouCord"><span>YouCord</span></a>
    <nav class="nav-links">
      <a href="#features">Fonctionnalités</a>
      <a href="#plugins">Plugins</a>
      <a href="#install">Installation</a>
      <a href="__GITHUB__" target="_blank" rel="noopener">GitHub</a>
    </nav>
    <div class="nav-cta">
      <a class="btn btn-gold" href="__DOWNLOAD__">⬇ <span class="lbl">Télécharger</span></a>
    </div>
  </div>
</header>

<a id="top"></a>
<section class="hero">
  <div class="wrap">
    <img class="hero-logo" src="data:image/png;base64,__ICON_B64__" alt="Logo YouCord">
    <h1 class="grad-text">YouCord</h1>
    <p class="tag">Everything Discord doesn't build, we create.</p>
    <p class="sub">Un client Discord personnalisé, rapide et sans bloat. Fork propre d'Equicord et Vencord — obfuscation retirée, démarrage plus léger, et tout l'écosystème de plugins.</p>
    <div class="hero-btns">
      <a class="btn btn-gold" href="__DOWNLOAD__">⬇ Télécharger le .exe</a>
      <a class="btn btn-ghost" href="#plugins">🧩 Voir les plugins</a>
      <a class="btn btn-purple" href="__TELEGRAM__" target="_blank" rel="noopener">✈ Telegram</a>
    </div>
    <div class="meta-row">
      <span class="pill"><span class="dot g"></span>Version <b>v__VERSION__</b></span>
      <span class="pill">🪟 <b>Windows</b></span>
      <span class="pill"><span class="dot"></span>Licence <b>GPL-3.0</b></span>
      <span class="pill">🔄 <b>Auto-updates</b></span>
    </div>

    <div class="trust">
      <span class="ic">🛡️</span>
      <p><b>Version propre &amp; sécurisée.</b> L'ancien YouCord d'origine a été compromis (vol de tokens). Cette version en est un fork nettoyé : le code malveillant a été entièrement retiré. Utilisez uniquement cette version.</p>
    </div>
  </div>
</section>

<div class="wrap">
    <div class="stats">
      <div class="stat"><div class="num grad-text" data-count="380">380</div><div class="lbl">Plugins disponibles</div></div>
      <div class="stat"><div class="num grad-text" id="win-count" data-count="0">0</div><div class="lbl">Téléchargements Windows</div></div>
      <div class="stat"><div class="num grad-text" id="mac-count" data-count="0">0</div><div class="lbl">Téléchargements macOS</div></div>
      <div class="stat"><div class="num grad-text">∞</div><div class="lbl">Personnalisation</div></div>
    </div>
</div>

<section id="features">
  <div class="wrap">
    <div class="sec-head">
      <div class="kicker">Pourquoi YouCord</div>
      <h2>Discord, en mieux.</h2>
      <p>On a retiré l'obfuscation, nettoyé le code, ajouté nos améliorations et gardé ce qui marche. Pas de bloat, pas de bêtises.</p>
    </div>
    <div class="feat-grid">
      <div class="feat"><div class="fic">⚡</div><h3>Démarrage rapide</h3><p>Sans obfuscation, le client se charge nettement plus vite et consomme moins de CPU et de RAM.</p></div>
      <div class="feat"><div class="fic">🔄</div><h3>Mises à jour auto</h3><p>Vérifie les updates en arrière-plan au lancement et les applique silencieusement.</p></div>
      <div class="feat"><div class="fic">🧩</div><h3>Support des plugins</h3><p>Compatible avec l'écosystème existant. Installe des plugins communautaires directement via des liens Git.</p></div>
      <div class="feat"><div class="fic">🔊</div><h3>Meilleur audio</h3><p>Modules vocaux optimisés pour un son plus clair et plus fort dès l'installation.</p></div>
      <div class="feat"><div class="fic">🎨</div><h3>Style personnalisé</h3><p>Interface plus fluide, icônes custom et de nombreuses améliorations de confort.</p></div>
      <div class="feat"><div class="fic">🔓</div><h3>Open source</h3><p>Code sous licence GPL-3.0, transparent et auditable. Construit avec la communauté.</p></div>
    </div>
  </div>
</section>

<section id="plugins" style="background:var(--bg-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-head">
      <div class="kicker">Écosystème</div>
      <h2>Les plugins en cours</h2>
      <p>Parcours les <b>380 plugins</b> intégrés à YouCord. Filtre par catégorie ou cherche par nom.</p>
    </div>
    <div class="plug-controls">
      <div class="search-box">
        <span class="si">🔍</span>
        <input id="search" type="text" placeholder="Rechercher un plugin (nom ou description)…" autocomplete="off">
      </div>
      <div class="chips" id="chips"></div>
    </div>
    <div class="count-row" id="count"></div>
    <div class="plug-grid" id="grid"></div>
    <button class="btn btn-ghost load-more" id="loadmore" style="display:none">Afficher plus de plugins</button>
  </div>
</section>

<section id="install">
  <div class="wrap">
    <div class="sec-head">
      <div class="kicker">Installation</div>
      <h2>Installe en 30 secondes</h2>
      <p>Windows, macOS et Linux. Choisis ta méthode.</p>
    </div>
    <div class="install-grid">
      <div class="icard">
        <h3>⬇ Méthode 1 — L'installeur .exe</h3>
        <div class="step"><span class="n">1</span><span>Télécharge <b>YouCord Setup (.exe)</b> depuis le bouton ci-dessous.</span></div>
        <div class="step"><span class="n">2</span><span>Lance l'exécutable et laisse-le injecter YouCord dans Discord.</span></div>
        <div class="step"><span class="n">3</span><span>Redémarre Discord — c'est prêt.</span></div>
        <a class="btn btn-gold" style="margin-top:8px" href="__DOWNLOAD__">⬇ Télécharger le .exe</a>
        <p class="tiny">Pas de release ? <a href="__RELEASES__" target="_blank" rel="noopener" style="color:var(--gold)">Voir toutes les versions sur GitHub →</a></p>
      </div>
      <div class="icard">
        <h3><i class="bi-apple"></i> Méthode 2 — macOS .dmg</h3>
        <div class="step"><span class="n">1</span><span>Télécharge le <b>.dmg</b> pour ton architecture ci-dessous.</span></div>
        <div class="step"><span class="n">2</span><span>Ouvre le fichier et glisse <b>YouCord</b> dans le dossier <b>Applications</b>.</span></div>
        <div class="step"><span class="n">3</span><span>Ouvre YouCord depuis le dossier Applications — c'est prêt.</span></div>
        <div style="display:flex;gap:10px;margin-top:8px;flex-wrap:wrap">
          <a class="btn btn-purple" id="mac-arm-btn" href="__RELEASES__" target="_blank" rel="noopener"><i class="bi-download"></i> Apple Silicon</a>
          <a class="btn btn-purple" id="mac-intel-btn" href="__RELEASES__" target="_blank" rel="noopener"><i class="bi-download"></i> Intel (x64)</a>
        </div>
        <p class="tiny">Besoin d'aide ? <a href="https://support.apple.com/fr-fr/HT211814" target="_blank" rel="noopener" style="color:var(--gold)">Vérifie ton processeur →</a></p>
      </div>
      <div class="icard">
        <h3>⚙ Méthode 3 — PowerShell / Linux</h3>
        <div class="step"><span class="n">1</span><span>Télécharge <b>youcord-install.ps1</b> depuis le dépôt.</span></div>
        <div class="step"><span class="n">2</span><span>Clic droit → <b>Exécuter avec PowerShell</b>.</span></div>
        <div class="step"><span class="n">3</span><span>Suis les étapes, redémarre Discord, terminé.</span></div>
        <div class="code"><button class="copy" data-copy="git clone https://github.com/nightcordlegit/youcord.git">Copier</button>git clone https://github.com/nightcordlegit/youcord.git</div>
        <p class="tiny">Build depuis les sources : <code>pnpm install</code> puis <code>pnpm build</code> puis <code>pnpm inject</code>.</p>
      </div>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <a class="brand" href="#top"><img src="data:image/png;base64,__ICON_B64__" alt="YouCord"><span>YouCord</span></a>
        <p>Un client Discord personnalisé, rapide et open source. Construit sur le travail formidable d'Equicord et Vencord.</p>
      </div>
      <div class="foot-links">
        <div class="foot-col">
          <h5>Projet</h5>
          <a href="__GITHUB__" target="_blank" rel="noopener">GitHub</a>
          <a href="__RELEASES__" target="_blank" rel="noopener">Téléchargements</a>
          <a href="__SITE__" target="_blank" rel="noopener">youcord.fr</a>
          <a href="#plugins">Plugins</a>
        </div>
        <div class="foot-col">
          <h5>Communauté</h5>
          <a href="__TELEGRAM__" target="_blank" rel="noopener">Telegram</a>
          <a href="https://github.com/Equicord/Equicord" target="_blank" rel="noopener">Equicord</a>
          <a href="https://github.com/Vendicated/Vencord" target="_blank" rel="noopener">Vencord</a>
        </div>
      </div>
    </div>
    <div class="disc">
      YouCord n'est pas affilié à Discord Inc. — L'utilisation de clients tiers est techniquement contraire aux conditions d'utilisation de Discord ; utilisez-le à vos risques.<br>
      Basé sur Equicord &amp; Vencord. Licence GPL-3.0. © 2026 YouCord.
    </div>
  </div>
</footer>

<script>
const PLUGINS = __PLUGINS_JSON__;
const CATS = [...new Set(PLUGINS.flatMap(p=>p.t))].sort();
const PAGE = 60;
let activeCat = "all", ycOnly = false, query = "", shown = PAGE;

const grid = document.getElementById('grid');
const countEl = document.getElementById('count');
const chipsEl = document.getElementById('chips');
const loadMore = document.getElementById('loadmore');
const searchEl = document.getElementById('search');

// build chips
function chip(label, key, cls){
  const c = document.createElement('span');
  c.className = 'chip' + (cls||'') + (key===activeCat?' active':'');
  c.textContent = label; c.dataset.key = key;
  chipsEl.appendChild(c); return c;
}
chip('Tous ('+PLUGINS.length+')','all');
const ycChip = chip('★ YouCord','__yc__','yc');
CATS.forEach(cat=>{
  const n = PLUGINS.filter(p=>p.t.includes(cat)).length;
  chip(cat+' ('+n+')', cat);
});

chipsEl.addEventListener('click', e=>{
  const c = e.target.closest('.chip'); if(!c) return;
  if(c.dataset.key==='__yc__'){
    ycOnly = !ycOnly; c.classList.toggle('active', ycOnly);
  } else {
    activeCat = c.dataset.key;
    document.querySelectorAll('.chip:not(.yc)').forEach(x=>x.classList.toggle('active', x.dataset.key===activeCat));
  }
  shown = PAGE; render();
});

let t=null;
searchEl.addEventListener('input', e=>{
  clearTimeout(t);
  t = setTimeout(()=>{ query = e.target.value.trim().toLowerCase(); shown = PAGE; render(); }, 130);
});

function filtered(){
  return PLUGINS.filter(p=>{
    if(ycOnly && !p.yc) return false;
    if(activeCat!=='all' && !p.t.includes(activeCat)) return false;
    if(query){
      const hay = (p.n+' '+p.d+' '+p.a.join(' ')).toLowerCase();
      if(!hay.includes(query)) return false;
    }
    return true;
  });
}

function esc(s){return (s||'').replace(/[&<>"]/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]));}

function render(){
  const list = filtered();
  const slice = list.slice(0, shown);
  countEl.innerHTML = '<b>'+list.length+'</b> plugin'+(list.length>1?'s':'')+(activeCat!=='all'?' — '+esc(activeCat):'')+(ycOnly?' · signés YouCord':'');
  if(list.length===0){
    grid.innerHTML = '<div class="no-res">Aucun plugin ne correspond à ta recherche.</div>';
    loadMore.style.display='none'; return;
  }
  grid.innerHTML = slice.map(p=>{
    const badges = (p.yc?'<span class="badge yc">YouCord</span>':'')
      + (p.core?'<span class="badge core">Core</span>':'')
      + (p.def?'<span class="badge on">Actif</span>':'');
    const tags = p.t.slice(0,3).map(x=>'<span class="ptag">'+esc(x)+'</span>').join('');
    return '<div class="pcard"><div class="pcard-top"><h4>'+esc(p.n)+'</h4>'+badges+'</div>'
      + '<p>'+esc(p.d||'—')+'</p>'
      + '<div class="ptags">'+tags+'</div>'
      + (p.a.length?'<div class="pauth">par '+esc(p.a.join(', '))+'</div>':'')
      + '</div>';
  }).join('');
  loadMore.style.display = list.length>shown ? 'block' : 'none';
}

loadMore.addEventListener('click', ()=>{ shown += PAGE; render(); });

// copy buttons
document.addEventListener('click', e=>{
  const b = e.target.closest('.copy'); if(!b) return;
  navigator.clipboard.writeText(b.dataset.copy).then(()=>{
    const o=b.textContent; b.textContent='Copié ✓'; setTimeout(()=>b.textContent=o,1400);
  });
});

// count-up stats
function animate(el){
  const target = +el.dataset.count; let cur=0;
  const step = Math.max(1, Math.round(target/40));
  const iv = setInterval(()=>{ cur+=step; if(cur>=target){cur=target;clearInterval(iv);} el.textContent=cur; }, 24);
}
function observeStats(){
  const io = new IntersectionObserver(es=>es.forEach(en=>{if(en.isIntersecting){animate(en.target);io.unobserve(en.target);}}));
  document.querySelectorAll('[data-count]').forEach(el=>io.observe(el));
}
observeStats();

// Fetch GitHub download counts & Mac DMG URLs
async function fetchGitHubStats() {
  try {
    const res = await fetch('https://api.github.com/repos/nightcordlegit/youcord/releases?per_page=100');
    if (!res.ok) throw new Error('HTTP ' + res.status);
    const releases = await res.json();
    let winCount = 0, macCount = 0;
    let latest = releases[0];

    for (const r of releases) {
      if (!r.assets) continue;
      for (const a of r.assets) {
        if (a.name.endsWith('.exe')) winCount += a.download_count;
        else if (a.name.endsWith('.dmg')) macCount += a.download_count;
      }
    }

    document.getElementById('win-count').dataset.count = winCount;
    document.getElementById('mac-count').dataset.count = macCount;
    animate(document.getElementById('win-count'));
    animate(document.getElementById('mac-count'));

    // Set Mac DMG download URLs from latest release
    if (latest && latest.assets) {
      for (const a of latest.assets) {
        if (a.name.endsWith('-arm64.dmg')) document.getElementById('mac-arm-btn').href = a.browser_download_url;
        else if (a.name.endsWith('-x64.dmg')) document.getElementById('mac-intel-btn').href = a.browser_download_url;
      }
    }
  } catch (e) {
    console.warn('Stats API indisponible, valeurs par défaut conservées.', e);
  }
}
fetchGitHubStats();

render();
</script>
</body>
</html>
"""

HTML = (HTML
  .replace("__ICON_B64__", icon_b64)
  .replace("__DOWNLOAD__", DOWNLOAD_URL)
  .replace("__RELEASES__", RELEASES_URL)
  .replace("__GITHUB__", GITHUB_URL)
  .replace("__TELEGRAM__", TELEGRAM_URL)
  .replace("__SITE__", SITE_URL)
  .replace("__VERSION__", VERSION)
  .replace("__PLUGINS_JSON__", json.dumps(plugins, ensure_ascii=False)))

open(f"{OUT}/index.html","w",encoding="utf-8").write(HTML)
print("index.html written:", os.path.getsize(f"{OUT}/index.html"), "bytes")
print("plugins embedded:", len(plugins))
