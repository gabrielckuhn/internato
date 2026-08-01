import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Horário Internato — Gabriel Kuhn", layout="wide")

# Ocultar o menu padrão do Streamlit para parecer mais com um site independente
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {
                padding-top: 0rem;
                padding-bottom: 0rem;
                padding-left: 0rem;
                padding-right: 0rem;
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# HTML original modificado
html_content = """<!DOCTYPE html>
<html lang="pt-BR" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Horário Internato — Gabriel Kuhn · 9º Período</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
/* ══════════════════════════════════════════
   DARK THEME (default)
══════════════════════════════════════════ */
[data-theme="dark"] {
  --bg-base: #14161C;
  --bg-glow-1: rgba(56,139,253,0.08);
  --bg-glow-2: rgba(48,213,136,0.07);
  --bg-glow-3: rgba(168,85,247,0.06);
  --bg-glow-4: rgba(230,57,70,0.06);
  --glass-bg: rgba(20, 22, 28, 0.55);
  --glass-hover: rgba(30, 34, 44, 0.78);
  --glass-border: rgba(255,255,255,0.10);
  --glass-inset: 0 1px 0 0 rgba(255,255,255,0.14) inset, 0 0 0 0.5px rgba(255,255,255,0.10) inset;
  --glass-shadow: 0 20px 60px -22px rgba(0,0,0,0.55);
  --text-primary: rgba(255,255,255,0.95);
  --text-secondary: rgba(255,255,255,0.62);
  --text-tertiary: rgba(255,255,255,0.35);
  --divider: rgba(255,255,255,0.06);
  --th-bg: rgba(255,255,255,0.04);
  --th-text: rgba(255,255,255,0.38);
  --th-hover-bg: rgba(255,255,255,0.14);
  --th-hover-text: rgba(255,255,255,0.95);

  --ped-color: rgba(56,139,253,0.18);
  --ped-bg-cell: rgba(56,139,253,0.11);
  --ped-border: rgba(56,139,253,0.45);
  --ped-text: #7ab8ff;
  --ped-section-border: rgba(56,139,253,0.28);

  --psf10-color: rgba(48,213,136,0.15);
  --psf10-bg-cell: rgba(48,213,136,0.10);
  --psf10-border: rgba(48,213,136,0.40);
  --psf10-text: #5de8a4;
  --psf10-section-border: rgba(48,213,136,0.24);

  --psf2-color: rgba(168,85,247,0.15);
  --psf2-bg-cell: rgba(168,85,247,0.10);
  --psf2-border: rgba(168,85,247,0.40);
  --psf2-text: #c084fc;
  --psf2-section-border: rgba(168,85,247,0.24);

  --turn-morning: #ffd24e;
  --turn-afternoon: #7ab8ff;
  --turn-night: #c084fc;
  --free-color: rgba(255,255,255,0.28);
  --loc-bg: rgba(255,255,255,0.08);
  --loc-border: rgba(255,255,255,0.14);
  --loc-text: rgba(255,255,255,0.72);
  --nav-bg: rgba(255,255,255,0.06);
  --nav-border: rgba(255,255,255,0.12);
  --nav-text: rgba(255,255,255,0.55);
  --footer-border: rgba(255,255,255,0.07);
  --footer-text: rgba(255,255,255,0.30);
  --switch-bg: rgba(255,255,255,0.08);
  --switch-track-on: #388bfd;
  --empty-opacity: 0.40;
  --today-bg: rgba(168,85,247,0.12);
  --today-bg-strong: rgba(168,85,247,0.18);
  --today-border: rgba(168,85,247,0.45);
  --today-text: #c084fc;
  --week-done-track: rgba(48,213,136,0.35);
  --week-done-knob: #30d588;
  --week-done-opacity: 0.20;
  --week-done-opacity-hover: 0.55;
}

/* ══════════════════════════════════════════
   LIGHT THEME
══════════════════════════════════════════ */
[data-theme="light"] {
  --bg-base: #f0f2f7;
  --bg-glow-1: rgba(56,139,253,0.10);
  --bg-glow-2: rgba(48,213,136,0.09);
  --bg-glow-3: rgba(168,85,247,0.08);
  --bg-glow-4: rgba(230,57,70,0.07);
  --glass-bg: rgba(255,255,255,0.72);
  --glass-hover: rgba(255,255,255,0.90);
  --glass-border: rgba(0,0,0,0.09);
  --glass-inset: 0 1px 0 0 rgba(255,255,255,0.90) inset, 0 0 0 0.5px rgba(0,0,0,0.07) inset;
  --glass-shadow: 0 8px 32px -10px rgba(0,0,0,0.14);
  --text-primary: rgba(15,18,28,0.92);
  --text-secondary: rgba(15,18,28,0.60);
  --text-tertiary: rgba(15,18,28,0.40);
  --divider: rgba(0,0,0,0.07);
  --th-bg: rgba(0,0,0,0.04);
  --th-text: rgba(0,0,0,0.40);
  --th-hover-bg: rgba(0,0,0,0.13);
  --th-hover-text: rgba(15,18,28,0.96);

  --ped-color: rgba(56,139,253,0.12);
  --ped-bg-cell: rgba(56,139,253,0.08);
  --ped-border: rgba(56,139,253,0.40);
  --ped-text: #1a6ec7;
  --ped-section-border: rgba(56,139,253,0.30);

  --psf10-color: rgba(16,153,90,0.12);
  --psf10-bg-cell: rgba(16,153,90,0.08);
  --psf10-border: rgba(16,153,90,0.38);
  --psf10-text: #0d7a4e;
  --psf10-section-border: rgba(16,153,90,0.25);

  --psf2-color: rgba(130,55,210,0.12);
  --psf2-bg-cell: rgba(130,55,210,0.08);
  --psf2-border: rgba(130,55,210,0.38);
  --psf2-text: #7428c8;
  --psf2-section-border: rgba(130,55,210,0.25);

  --turn-morning: #b5830a;
  --turn-afternoon: #1a6ec7;
  --turn-night: #7428c8;
  --free-color: rgba(0,0,0,0.32);
  --loc-bg: rgba(0,0,0,0.05);
  --loc-border: rgba(0,0,0,0.12);
  --loc-text: rgba(0,0,0,0.60);
  --nav-bg: rgba(0,0,0,0.05);
  --nav-border: rgba(0,0,0,0.12);
  --nav-text: rgba(0,0,0,0.55);
  --footer-border: rgba(0,0,0,0.10);
  --footer-text: rgba(0,0,0,0.38);
  --switch-bg: rgba(0,0,0,0.08);
  --switch-track-on: #388bfd;
  --empty-opacity: 0.45;
  --today-bg: rgba(147,51,234,0.08);
  --today-bg-strong: rgba(147,51,234,0.12);
  --today-border: rgba(147,51,234,0.30);
  --today-text: #7e22ce;
  --week-done-track: rgba(16,153,90,0.30);
  --week-done-knob: #10995a;
  --week-done-opacity: 0.24;
  --week-done-opacity-hover: 0.6;
}

/* ══════════════════════════════════════════
   BASE
══════════════════════════════════════════ */
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{
  background:var(--bg-base);
  color:var(--text-primary);
  font-family:'Inter',system-ui,sans-serif;
  font-size:14px;
  line-height:1.6;
  min-height:100vh;
  overflow-x:clip;
  transition: background 0.35s ease, color 0.35s ease;
}
body::before{
  content:'';
  position:fixed;inset:0;
  background:
    radial-gradient(ellipse 80% 50% at 10% 20%, var(--bg-glow-1) 0%,transparent 60%),
    radial-gradient(ellipse 60% 40% at 85% 10%, var(--bg-glow-2) 0%,transparent 55%),
    radial-gradient(ellipse 70% 60% at 50% 90%, var(--bg-glow-3) 0%,transparent 60%),
    radial-gradient(ellipse 50% 40% at 90% 70%, var(--bg-glow-4) 0%,transparent 50%);
  z-index:0;pointer-events:none;
  transition: background 0.35s ease;
}
.wrapper{position:relative;z-index:1;max-width:1180px;margin:0 auto;padding:2.5rem 1.5rem 4rem;}

/* ══════════════════════════════════════════
   THEME SWITCH
══════════════════════════════════════════ */
.theme-switch-wrap{
  position:fixed;top:1.25rem;right:1.5rem;z-index:1000;
  display:flex;align-items:center;gap:0.6rem;
  background:var(--glass-bg);
  backdrop-filter:blur(24px) saturate(180%);
  -webkit-backdrop-filter:blur(24px) saturate(180%);
  border:0.5px solid var(--glass-border);
  box-shadow:var(--glass-inset),var(--glass-shadow);
  border-radius:100px;
  padding:0.35rem 0.85rem;
  transition: background 0.3s ease, border-color 0.3s ease;
}
.theme-switch-label{font-size:11px;font-weight:500;letter-spacing:0.07em;color:var(--text-secondary);user-select:none;white-space:nowrap;}
.theme-switch{position:relative;display:inline-block;width:40px;height:22px;cursor:pointer;}
.theme-switch input{opacity:0;width:0;height:0;}
.theme-track{
  position:absolute;inset:0;
  background:var(--switch-bg);
  border-radius:100px;
  border:0.5px solid var(--glass-border);
  transition: background 0.3s ease;
}
.theme-track::after{
  content:'';position:absolute;
  top:3px;left:3px;
  width:16px;height:16px;
  border-radius:50%;
  background:#888;
  transition: transform 0.25s ease, background 0.25s ease;
}
.theme-switch input:checked + .theme-track{background:rgba(56,139,253,0.25);}
.theme-switch input:checked + .theme-track::after{transform:translateX(18px);background:var(--switch-track-on);}
.sun-icon,.moon-icon{font-size:14px;line-height:1;}

/* ══════════════════════════════════════════
   HEADER
══════════════════════════════════════════ */
.page-header{
  text-align:center;margin-bottom:2.5rem;
  padding:2.5rem 2rem;
  background:var(--glass-bg);
  backdrop-filter:blur(44px) saturate(180%);
  -webkit-backdrop-filter:blur(44px) saturate(180%);
  border-radius:1.25rem;
  box-shadow:var(--glass-inset),var(--glass-shadow);
  border:0.5px solid var(--glass-border);
  position:relative;overflow:hidden;
  transition: background 0.35s ease;
}
.page-header::after{
  content:'';position:absolute;top:-60px;right:-60px;
  width:200px;height:200px;
  background:radial-gradient(circle,rgba(56,139,253,0.13) 0%,transparent 70%);
  border-radius:50%;pointer-events:none;
}
.eyebrow{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:0.18em;text-transform:uppercase;color:var(--text-secondary);margin-bottom:0.6rem;}
.page-title{
  font-size:clamp(1.6rem,4vw,2.4rem);font-weight:700;
  background:linear-gradient(135deg,var(--text-primary) 0%,var(--text-secondary) 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  line-height:1.2;margin-bottom:0.5rem;
}
.page-subtitle{font-size:13px;color:var(--text-secondary);letter-spacing:0.03em;}
.badge-row{display:flex;justify-content:center;gap:0.6rem;flex-wrap:wrap;margin-top:1.2rem;}
.badge{display:inline-flex;align-items:center;gap:0.4rem;padding:0.28rem 0.85rem;border-radius:100px;font-size:11.5px;font-weight:500;letter-spacing:0.04em;border:0.5px solid;}
.badge-ped{background:var(--ped-color);border-color:var(--ped-border);color:var(--ped-text);}
.badge-psf10{background:var(--psf10-color);border-color:var(--psf10-border);color:var(--psf10-text);}
.badge-psf2{background:var(--psf2-color);border-color:var(--psf2-border);color:var(--psf2-text);}
.dot{width:6px;height:6px;border-radius:50%;display:inline-block;}
.dot-ped{background:#388bfd;}.dot-psf10{background:#30d588;}.dot-psf2{background:#a855f7;}

/* ══════════════════════════════════════════
   USER SELECT (progresso individual)
══════════════════════════════════════════ */
.user-select-row{
  display:flex;justify-content:center;align-items:center;
  gap:0.5rem;flex-wrap:wrap;margin-top:1.1rem;
  padding-top:1.1rem;
  border-top:0.5px solid var(--footer-border);
}
.user-select-label{
  font-family:'JetBrains Mono',monospace;
  font-size:10.5px;letter-spacing:0.08em;text-transform:uppercase;
  color:var(--text-tertiary);margin-right:0.2rem;white-space:nowrap;
}
.user-badge{
  font-family:'Inter',sans-serif;
  padding:0.32rem 0.95rem;border-radius:100px;
  font-size:12px;font-weight:600;letter-spacing:0.01em;
  border:0.5px solid var(--glass-border);
  background:var(--glass-bg);
  color:var(--text-secondary);
  cursor:pointer;
  transition: background 0.2s ease, color 0.2s ease, border-color 0.2s ease, transform 0.15s ease;
}
.user-badge:hover{background:var(--glass-hover);color:var(--text-primary);}
.user-badge:active{transform:scale(0.96);}
.user-badge.active{
  background:var(--ped-color);
  border-color:var(--ped-border);
  color:var(--ped-text);
}

/* ══════════════════════════════════════════
   WEEK-DONE SWITCH (marcar semana como concluída)
   — vive na 1ª coluna da linha dos dias, entre
     "Turno / Dia" e "☀️ 07h · 12h" —
══════════════════════════════════════════ */
.cross-table .day-header-row th.week-switch-cell{
  vertical-align:middle;
}
.week-switch{
  position:relative;display:inline-flex;align-items:center;
  width:32px;height:17px;cursor:pointer;flex-shrink:0;
}
.week-switch input{position:absolute;opacity:0;width:0;height:0;}
.week-switch-track{
  position:absolute;inset:0;
  background:var(--switch-bg);
  border-radius:100px;
  border:0.5px solid var(--glass-border);
  transition:background 0.3s ease;
}
.week-switch-track::after{
  content:'';position:absolute;
  top:2px;left:2.5px;width:12px;height:12px;
  border-radius:50%;background:#888;
  transition:transform 0.25s ease,background 0.25s ease;
}
.week-switch-icon{
  position:absolute;left:4px;top:50%;
  transform:translateY(-50%);
  font-size:8px;line-height:1;font-weight:700;
  color:#fff;opacity:0;
  transition:opacity 0.2s ease;
  pointer-events:none;
}
.week-switch input:checked + .week-switch-track{background:var(--week-done-track);}
.week-switch input:checked + .week-switch-track::after{transform:translateX(15px);background:var(--week-done-knob);}
.week-switch input:checked ~ .week-switch-icon{opacity:1;}

/* Estado "semana concluída": esmaece o card inteiro e aplica um
   véu na cor do próprio rodízio (azul=PED, verde=PSF10, roxo=PSF2)
   em vez de um dessaturado acastanhado. */
.cross-table-wrap{position:relative;}
.cross-table-wrap.week-done{
  opacity:var(--week-done-opacity);
  transition:opacity 0.35s ease;
}
.cross-table-wrap.week-done::after{
  content:'';
  position:absolute;inset:0;
  border-radius:inherit;
  pointer-events:none;
  z-index:3;
}
[data-theme="dark"] .cross-table-wrap.week-done::after { background: rgba(255, 255, 255, 0.12); }
[data-theme="light"] .cross-table-wrap.week-done::after { background: rgba(255, 255, 255, 0.5); }
.cross-table-wrap.week-done:hover{opacity:var(--week-done-opacity-hover);}

/* ══════════════════════════════════════════
   TODAY HIGHLIGHT (coluna do dia atual)
══════════════════════════════════════════ */
.cross-table thead tr.day-header-row th.today-col{
  background:var(--today-bg-strong) !important;
  color:var(--today-text) !important;
  font-weight:700;
  box-shadow:inset 1px 0 0 0 var(--today-border), inset -1px 0 0 0 var(--today-border), inset 0 -2px 0 0 var(--today-border);
}
.cross-table tbody tr td.data-cell.today-col{
  background:var(--today-bg) !important;
  box-shadow:inset 1px 0 0 0 var(--today-border), inset -1px 0 0 0 var(--today-border);
}
.cross-table tbody tr:last-child td.data-cell.today-col{
  box-shadow:inset 1px 0 0 0 var(--today-border), inset -1px 0 0 0 var(--today-border), inset 0 -2px 0 0 var(--today-border);
}

/* ══════════════════════════════════════════
   RODIZIO TABS (seletor com indicador deslizante)
══════════════════════════════════════════ */
:root{
  --tab-ped: #388bfd;
  --tab-psf10: #30d588;
  --tab-psf2: #a855f7;
}
.rodizio-tabs{
  position:relative;
  display:flex;flex-wrap:wrap;gap:0.35rem;
  padding:0.45rem;
  margin-bottom:2.5rem;
  background:var(--glass-bg);
  backdrop-filter:blur(44px) saturate(180%);
  -webkit-backdrop-filter:blur(44px) saturate(180%);
  border-radius:1.1rem;
  border:0.5px solid var(--glass-border);
  box-shadow:var(--glass-inset),var(--glass-shadow);
  transition: background 0.35s ease;
}
.rodizio-tab-indicator{
  position:absolute;
  top:0.45rem;left:0.45rem;
  height:calc(100% - 0.9rem);
  width:0;
  border-radius:0.7rem;
  background:var(--tab-ped);
  box-shadow:0 6px 16px -4px rgba(0,0,0,0.35);
  transition: transform 0.4s cubic-bezier(.65,0,.35,1), width 0.4s cubic-bezier(.65,0,.35,1), background-color 0.4s ease;
  z-index:1;
  pointer-events:none;
}
.rodizio-tab-btn{
  position:relative;z-index:2;
  display:flex;flex-direction:column;align-items:flex-start;gap:0.18rem;
  padding:0.55rem 1.1rem;
  border-radius:0.7rem;
  border:none;background:transparent;
  cursor:pointer;text-align:left;
  font-family:'Inter',sans-serif;
  flex:1 1 auto;min-width:fit-content;
  transition: background 0.2s ease;
}
.rodizio-tab-btn .tab-eyebrow{
  display:block;
  font-family:'JetBrains Mono',monospace;
  font-size:10px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;
  color:var(--text-tertiary);
  white-space:nowrap;
  transition: color 0.3s ease;
}
.rodizio-tab-btn .tab-title{
  display:block;
  font-size:13px;font-weight:600;
  color:var(--text-secondary);
  white-space:nowrap;
  transition: color 0.3s ease;
}
.rodizio-tab-btn:hover:not(.active){background:var(--glass-hover);}
.rodizio-tab-btn:hover:not(.active) .tab-eyebrow,
.rodizio-tab-btn:hover:not(.active) .tab-title{color:var(--text-primary);}
.rodizio-tab-btn.active .tab-eyebrow{color:rgba(255,255,255,0.78);}
.rodizio-tab-btn.active .tab-title{color:#fff;}
.rodizio-panel.hidden{display:none;}

/* ══════════════════════════════════════════
   RODIZIO SECTION
══════════════════════════════════════════ */
.rodizio-section{margin-bottom:3.5rem;}
.rodizio-header{
  display:flex;align-items:center;gap:0.8rem 1rem;margin-bottom:1.5rem;
  padding:1rem 1.4rem;
  background:var(--glass-bg);
  backdrop-filter:blur(44px) saturate(180%);
  -webkit-backdrop-filter:blur(44px) saturate(180%);
  border-radius:0.9rem;
  box-shadow:var(--glass-inset),var(--glass-shadow);
  border:0.5px solid var(--glass-border);
  flex-wrap:wrap;
  transition: background 0.35s ease;
}
.rodizio-num{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:0.12em;color:var(--text-secondary);text-transform:uppercase;white-space:nowrap;}
.rodizio-title{font-size:1rem;font-weight:600;color:var(--text-primary);}
.rodizio-dates{font-family:'JetBrains Mono',monospace;font-size:11.5px;color:var(--text-secondary);margin-left:auto;white-space:nowrap;}
.disc-tag{padding:0.22rem 0.7rem;border-radius:100px;font-size:11px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;border:0.5px solid;}
.disc-ped{background:var(--ped-color);border-color:var(--ped-border);color:var(--ped-text);}
.disc-psf10{background:var(--psf10-color);border-color:var(--psf10-border);color:var(--psf10-text);}
.disc-psf2{background:var(--psf2-color);border-color:var(--psf2-border);color:var(--psf2-text);}

/* ══════════════════════════════════════════
   CROSS-TABLE (linhas = turno, colunas = semanas)
══════════════════════════════════════════ */
.week-tables-group{display:flex;flex-direction:column;gap:0.75rem;}
.cross-table-wrap{
  background:var(--glass-bg);
  backdrop-filter:blur(44px) saturate(180%);
  -webkit-backdrop-filter:blur(44px) saturate(180%);
  border-radius:1.25rem;
  box-shadow:var(--glass-inset),var(--glass-shadow);
  border:0.5px solid var(--glass-border);
  overflow:visible;
  transition: background 0.35s ease;
}
.cross-table-wrap:hover{background:var(--glass-hover);}
.cross-table-wrap.type-ped{border-color:var(--ped-section-border);}
.cross-table-wrap.type-psf10{border-color:var(--psf10-section-border);}
.cross-table-wrap.type-psf2{border-color:var(--psf2-section-border);}

.cross-table{width:100%;border-collapse:collapse;table-layout:fixed;}
.cross-table col.col-turno{width:140px;}
.cross-table col.col-day{width:calc((100% - 140px) / 6);}

/* Header row: semanas */
.cross-table thead tr th{
  background:var(--th-bg);
  padding:0.7rem 1rem;
  text-align:center;
  font-size:10.5px;font-weight:600;letter-spacing:0.09em;text-transform:uppercase;
  color:var(--th-text);
  border-bottom:0.5px solid var(--divider);
  white-space:nowrap;
  transition:background 0.15s ease,color 0.15s ease;
}
.cross-table thead tr th:first-child{
  text-align:left;
  border-right:0.5px solid var(--divider);
  padding-left:1.2rem;
}
.cross-table thead tr th.week-th{}
.cross-table thead tr th.week-th:hover{
  background:var(--th-hover-bg);
  color:var(--th-hover-text);
  cursor:default;
}

/* Sub-header: dia */
.cross-table .day-header-row th{
  background:var(--th-bg);
  padding:0.3rem 1rem;
  font-family:'JetBrains Mono',monospace;
  font-size:10px;font-weight:500;
  color:var(--text-tertiary);
  border-bottom:0.5px solid var(--divider);
  text-align:center;letter-spacing:0.06em;
  transition:background 0.15s ease,color 0.15s ease;
}
.cross-table .day-header-row th:first-child{border-right:0.5px solid var(--divider);padding-left:1.2rem;text-align:left;}
.cross-table .day-header-row th.week-switch-cell{padding-top:0.22rem;padding-bottom:0.22rem;}
.cross-table .day-header-row th:not(:first-child):hover{
  background:var(--th-hover-bg);
  color:var(--th-hover-text);
  cursor:default;
}

/* Row header: turno */
.cross-table tbody tr td.row-header{
  font-family:'JetBrains Mono',monospace;
  font-size:11px;font-weight:600;
  padding:0.8rem 0.85rem 0.8rem 1.1rem;
  white-space:nowrap;
  border-right:0.5px solid var(--divider);
  border-bottom:0.5px solid var(--divider);
  vertical-align:middle;
  background:var(--th-bg);
}
.turn-emoji{
  font-size:15px;
  line-height:1;
  vertical-align:middle;
  margin-right:0.32em;
  display:inline-block;
}
.turn-time{
  font-size:12.5px;
  font-weight:600;
  letter-spacing:0.01em;
  vertical-align:middle;
}
.row-header.turn-morning{color:var(--turn-morning);}
.row-header.turn-afternoon{color:var(--turn-afternoon);}
.row-header.turn-night{color:var(--turn-night);}
.row-header.turn-day{color:var(--text-tertiary);}

/* Data cells */
.cross-table tbody tr td.data-cell{
  padding:0.75rem 0.9rem;
  vertical-align:top;
  border-bottom:0.5px solid var(--divider);
  border-right:0.5px solid var(--divider);
  font-size:12.5px;
  transition: background 0.15s ease;
}
.cross-table tbody tr td.data-cell:last-child{border-right:none;}
.cross-table tbody tr:last-child td{border-bottom:none;}
.cross-table tbody tr:hover td.data-cell{background:rgba(255,255,255,0.025);}
[data-theme="light"] .cross-table tbody tr:hover td.data-cell{background:rgba(0,0,0,0.025);}

/* Cell content */
.cell-free{font-size:11px;color:var(--free-color);font-style:italic;}
.cell-empty{opacity:var(--empty-opacity);}
.act-name{color:var(--text-primary);font-weight:600;font-size:12px;display:block;line-height:1.35;}
.act-detail{color:var(--text-secondary);font-size:11px;font-style:italic;display:block;}
.act-sub{color:var(--text-secondary);font-size:11.5px;display:block;}

/* Location chip */
.loc-chip{
  display:inline-block;
  margin-top:0.3rem;
  padding:0.18rem 0.55rem;
  border-radius:5px;
  font-size:10px;font-weight:600;
  letter-spacing:0.04em;
  background:var(--loc-bg);
  border:0.5px solid var(--loc-border);
  color:var(--loc-text);
  white-space:normal;
  line-height:1.4;
}
/* Colored location chips per discipline */
.loc-ped{background:var(--ped-bg-cell);border-color:var(--ped-border);color:var(--ped-text);}
.loc-psf10{background:var(--psf10-bg-cell);border-color:var(--psf10-border);color:var(--psf10-text);}
.loc-psf2{background:var(--psf2-bg-cell);border-color:var(--psf2-border);color:var(--psf2-text);}

/* Row separators between day groups */
.cross-table .sep-row td{
  padding:0;height:4px;
  background:var(--divider);
  border-top:none;border-bottom:none;
}

/* Day label in row header */
.day-label-cell{
  background:var(--th-bg) !important;
  border-right:0.5px solid var(--divider) !important;
  padding:0.5rem 1rem 0.5rem 1.2rem !important;
  vertical-align:middle !important;
}
.day-label{
  font-family:'JetBrains Mono',monospace;
  font-size:10px;font-weight:500;
  color:var(--text-tertiary);
  letter-spacing:0.08em;
  text-transform:uppercase;
  white-space:nowrap;
}
/* Weekend day row */
.cross-table .weekend-row td{opacity:0.55;}

/* ══════════════════════════════════════════
   FOOTER
══════════════════════════════════════════ */
.page-footer{
  text-align:center;margin-top:3rem;padding-top:2rem;
  border-top:0.5px solid var(--footer-border);
  color:var(--footer-text);
  font-size:11px;font-family:'JetBrains Mono',monospace;letter-spacing:0.06em;
}
[id]{scroll-margin-top:1.5rem;}
@media(max-width:800px){
  .theme-switch-wrap{top:0.75rem;right:0.75rem;}
  .rodizio-dates{display:none;}
  .wrapper{padding-top:4rem;}

  /* Seletor de rodízios: rolagem horizontal em vez de quebrar feio */
  .rodizio-tabs{
    flex-wrap:nowrap;
    overflow-x:auto;
    -webkit-overflow-scrolling:touch;
  }
  .rodizio-tab-btn{flex:0 0 auto;}

  /* ─── Modo scroll automático (telas pequenas) ───
     Cada tabela de semana passa a rolar horizontalmente de forma
     independente, em vez de espremer as colunas e vazar conteúdo.
     As semanas continuam separadas, uma abaixo da outra. */
  .cross-table-wrap{
    overflow-x:auto;
    overflow-y:visible;
    -webkit-overflow-scrolling:touch;
  }
  .cross-table{
    table-layout:auto;
    min-width:760px;
  }
  .cross-table col.col-turno{width:auto;}
  .cross-table col.col-day{width:auto;}
  .cross-table thead tr th:first-child{min-width:120px;}
  .cross-table .day-header-row th:first-child{min-width:120px;}
  .cross-table tbody tr td.row-header{min-width:120px;}
  .cross-table tbody tr td.data-cell{min-width:110px;}
}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{transition:none!important;}}
</style>
</head>
<body>
<!-- THEME SWITCH -->
<div class="theme-switch-wrap">
  <span class="moon-icon">🌙</span>
  <label class="theme-switch" title="Alternar tema">
    <input type="checkbox" id="themeToggle">
    <span class="theme-track"></span>
  </label>
  <span class="sun-icon">☀️</span>
</div>

<div class="wrapper">

<!-- HEADER -->
<header class="page-header">
  <p class="eyebrow">Internato Médico · Turma XXIII · 9ª Etapa</p>
  <h1 class="page-title" id="pageTitle">Gabriel Kuhn</h1>
  <p class="page-subtitle">9º Período · 2026.2 &nbsp;·&nbsp; Grupo <strong>09-14</strong></p>
  <div class="badge-row">
    <span class="badge badge-ped"><span class="dot dot-ped"></span> PED A3 · PED A4 (SEM 1–7)</span>
    <span class="badge badge-psf10"><span class="dot dot-psf10"></span> PSF 10 (SEM 8–14 · até 18/10)</span>
    <span class="badge badge-psf2"><span class="dot dot-psf2"></span> PSF 2 (SEM 15–21 · até 06/12)</span>
  </div>
  <div class="user-select-row" id="userSelectRow">
    <span class="user-select-label">Progresso de:</span>
    <button class="user-badge" data-user="Fernando" data-fullname="Fernando Aranda" type="button">Fernando</button>
    <button class="user-badge" data-user="Gabriel" data-fullname="Gabriel Kuhn" type="button">Gabriel</button>
    <button class="user-badge" data-user="Miguel" data-fullname="Miguel Mafra" type="button">Miguel</button>
    <button class="user-badge" data-user="Newton" data-fullname="Newton Vital" type="button">Newton</button>
  </div>
</header>

<!-- SELETOR DE RODÍZIOS -->
<nav class="rodizio-tabs" id="rodizioTabs">
  <div class="rodizio-tab-indicator" id="tabIndicator"></div>
  <button class="rodizio-tab-btn active" data-target="tab-rod1" data-color="ped" type="button">
    <span class="tab-eyebrow">1º Rodízio (13/07 a 09/08)</span>
    <span class="tab-title">PED A3 (Ambulatório)</span>
  </button>
  <button class="rodizio-tab-btn" data-target="tab-rod2" data-color="ped" type="button">
    <span class="tab-eyebrow">2º Rodízio (10/08 a 30/08)</span>
    <span class="tab-title">PED A4 (UTIP · Crônicas)</span>
  </button>
  <button class="rodizio-tab-btn" data-target="tab-rod34" data-color="psf10" type="button">
    <span class="tab-eyebrow">3º e 4º Rodízio (31/08 a 18/10)</span>
    <span class="tab-title">PSF 10 (UBS Santa Terezinha)</span>
  </button>
  <button class="rodizio-tab-btn" data-target="tab-rod56" data-color="psf2" type="button">
    <span class="tab-eyebrow">5º e 6º Rodízio (19/10 a 06/12)</span>
    <span class="tab-title">PSF 2 (UBS Hugo Gurgel)</span>
  </button>
</nav>

<!-- ════════════ 1º RODÍZIO — PED A3 — SEM 1–4 ════════════ -->
<section class="rodizio-section rodizio-panel" id="tab-rod1">
  <div class="rodizio-header">
    <span class="rodizio-num">1º Rodízio</span>
    <span class="disc-tag disc-ped">PED A3</span>
    <span class="rodizio-title">Pediatria — Ambulatório Subespecialidades</span>
    <span class="rodizio-dates">13 Jul → 09 Ago 2026 · SEM 1–4</span>
  </div>
  <div class="week-tables-group">

  <!-- SEM 01 -->
  <div class="cross-table-wrap type-ped">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="6">SEM 01 &nbsp;·&nbsp; 13–18/07</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 01 como concluída"><input type="checkbox" class="week-done-toggle" data-week="01"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 13/07</th><th>Ter 14/07</th><th>Qua 15/07</th><th>Qui 16/07</th><th>Sex 17/07</th><th>Sáb 18/07</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">ANA CLARA</span><span class="act-sub">Gastroenterologia</span><span class="loc-chip loc-ped">AMB — Complexo UNIT</span></td>
        <td class="data-cell"><span class="act-name">TATIANA</span><span class="act-sub">Hebiatria</span><span class="loc-chip loc-ped">AMB — Complexo UNIT</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">VIVIANE</span><span class="act-sub">Cardiologia</span><span class="loc-chip loc-ped">Anexo Hosp. da Criança</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="act-name">CARLA ELLIS</span><span class="act-sub">Infectologia</span><span class="loc-chip loc-ped">AMB — HSI</span></td>
        <td class="data-cell"><span class="act-name">EDSON</span><span class="act-sub">Puericultura</span><span class="loc-chip loc-ped">AMB — HSI</span></td>
        <td class="data-cell"><span class="act-name">AUDREY</span><span class="act-sub">Nefrologia</span><span class="loc-chip loc-ped">AMB — Complexo UNIT</span></td>
        <td class="data-cell"><span class="act-name">PRISCILA</span><span class="act-sub">Pneumologia</span><span class="loc-chip loc-ped">AMB — Complexo UNIT</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-night"><span class="turn-emoji">🌙</span><span class="turn-time">19h&nbsp;·&nbsp;24h</span></td>
        <td class="data-cell"><span class="act-name">Conf. · ALINE</span><span class="loc-chip loc-ped">UNIT (15×15)</span></td>
        <td class="data-cell"><span class="act-name">Conf. · ANA JOVINA</span><span class="loc-chip loc-ped">UNIT (15×15)</span></td>
        <td class="data-cell"><span class="cell-free">—</span></td>
        <td class="data-cell"><span class="cell-free">—</span></td>
        <td class="data-cell"><span class="cell-free">—</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  <!-- SEM 02 -->
  <div class="cross-table-wrap type-ped">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="6">SEM 02 &nbsp;·&nbsp; 20–25/07</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 02 como concluída"><input type="checkbox" class="week-done-toggle" data-week="02"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 20/07</th><th>Ter 21/07</th><th>Qua 22/07</th><th>Qui 23/07</th><th>Sex 24/07</th><th>Sáb 25/07</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">ANA CLARA</span><span class="act-sub">Gastroenterologia</span><span class="loc-chip loc-ped">AMB — Complexo UNIT</span></td>
        <td class="data-cell"><span class="act-name">TATIANA</span><span class="act-sub">Hebiatria</span><span class="loc-chip loc-ped">AMB — Complexo UNIT</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">VIVIANE</span><span class="act-sub">Cardiologia</span><span class="loc-chip loc-ped">Anexo Hosp. da Criança</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="act-name">CARLA ELLIS</span><span class="act-sub">Infectologia</span><span class="loc-chip loc-ped">AMB — HSI</span></td>
        <td class="data-cell"><span class="act-name">EDSON</span><span class="act-sub">Puericultura</span><span class="loc-chip loc-ped">AMB — HSI</span></td>
        <td class="data-cell"><span class="act-name">AUDREY</span><span class="act-sub">Nefrologia</span><span class="loc-chip loc-ped">AMB — Complexo UNIT</span></td>
        <td class="data-cell"><span class="act-name">PRISCILA</span><span class="act-sub">Pneumologia</span><span class="loc-chip loc-ped">AMB — Complexo UNIT</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-night"><span class="turn-emoji">🌙</span><span class="turn-time">19h&nbsp;·&nbsp;24h</span></td>
        <td class="data-cell"><span class="act-name">Conf. · ALINE</span><span class="loc-chip loc-ped">UNIT (15×15)</span></td>
        <td class="data-cell"><span class="act-name">Conf. · ANA JOVINA</span><span class="loc-chip loc-ped">UNIT (15×15)</span></td>
        <td class="data-cell"><span class="cell-free">—</span></td>
        <td class="data-cell"><span class="cell-free">—</span></td>
        <td class="data-cell"><span class="cell-free">—</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  <!-- SEM 03 -->
  <div class="cross-table-wrap type-ped">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="6">SEM 03 &nbsp;·&nbsp; 27/07–01/08</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 03 como concluída"><input type="checkbox" class="week-done-toggle" data-week="03"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 27/07</th><th>Ter 28/07</th><th>Qua 29/07</th><th>Qui 30/07</th><th>Sex 31/07</th><th>Sáb 01/08</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">ANA CLARA</span><span class="act-sub">Gastroenterologia</span><span class="loc-chip loc-ped">AMB — Complexo UNIT</span></td>
        <td class="data-cell"><span class="act-name">TATIANA</span><span class="act-sub">Hebiatria</span><span class="loc-chip loc-ped">AMB — Complexo UNIT</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">VIVIANE</span><span class="act-sub">Cardiologia</span><span class="loc-chip loc-ped">Anexo Hosp. da Criança</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="act-name">CARLA ELLIS</span><span class="act-sub">Infectologia</span><span class="loc-chip loc-ped">AMB — HSI</span></td>
        <td class="data-cell"><span class="act-name">EDSON</span><span class="act-sub">Puericultura</span><span class="loc-chip loc-ped">AMB — HSI</span></td>
        <td class="data-cell"><span class="act-name">AUDREY</span><span class="act-sub">Nefrologia</span><span class="loc-chip loc-ped">AMB — Complexo UNIT</span></td>
        <td class="data-cell"><span class="act-name">PRISCILA</span><span class="act-sub">Pneumologia</span><span class="loc-chip loc-ped">AMB — Complexo UNIT</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-night"><span class="turn-emoji">🌙</span><span class="turn-time">19h&nbsp;·&nbsp;24h</span></td>
        <td class="data-cell"><span class="act-name">Conf. · ALINE</span><span class="loc-chip loc-ped">UNIT (15×15)</span></td>
        <td class="data-cell"><span class="act-name">Conf. · ANA JOVINA</span><span class="loc-chip loc-ped">UNIT (15×15)</span></td>
        <td class="data-cell"><span class="cell-free">—</span></td>
        <td class="data-cell"><span class="cell-free">—</span></td>
        <td class="data-cell"><span class="cell-free">—</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  <!-- SEM 04 -->
  <div class="cross-table-wrap type-ped">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="6">SEM 04 &nbsp;·&nbsp; 03–08/08</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 04 como concluída"><input type="checkbox" class="week-done-toggle" data-week="04"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 03/08</th><th>Ter 04/08</th><th>Qua 05/08</th><th>Qui 06/08</th><th>Sex 07/08</th><th>Sáb 08/08</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">ANA CLARA</span><span class="act-sub">Gastroenterologia</span><span class="loc-chip loc-ped">AMB — Complexo UNIT</span></td>
        <td class="data-cell"><span class="act-name">TATIANA</span><span class="act-sub">Hebiatria</span><span class="loc-chip loc-ped">AMB — Complexo UNIT</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">VIVIANE</span><span class="act-sub">Cardiologia</span><span class="loc-chip loc-ped">Anexo Hosp. da Criança</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="act-name">CARLA ELLIS</span><span class="act-sub">Infectologia</span><span class="loc-chip loc-ped">AMB — HSI</span></td>
        <td class="data-cell"><span class="act-name">EDSON</span><span class="act-sub">Puericultura</span><span class="loc-chip loc-ped">AMB — HSI</span></td>
        <td class="data-cell"><span class="act-name">AUDREY</span><span class="act-sub">Nefrologia</span><span class="loc-chip loc-ped">AMB — Complexo UNIT</span></td>
        <td class="data-cell"><span class="act-name">PRISCILA</span><span class="act-sub">Pneumologia</span><span class="loc-chip loc-ped">AMB — Complexo UNIT</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-night"><span class="turn-emoji">🌙</span><span class="turn-time">19h&nbsp;·&nbsp;24h</span></td>
        <td class="data-cell"><span class="act-name">Conf. · ALINE</span><span class="loc-chip loc-ped">UNIT (15×15)</span></td>
        <td class="data-cell"><span class="act-name">Conf. · ANA JOVINA</span><span class="loc-chip loc-ped">UNIT (15×15)</span></td>
        <td class="data-cell"><span class="cell-free">—</span></td>
        <td class="data-cell"><span class="cell-free">—</span></td>
        <td class="data-cell"><span class="cell-free">—</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  </div><!-- end week-tables-group -->
</section>

<!-- ════════════ 2º RODÍZIO — PED A4 — SEM 5–7 ════════════ -->
<section class="rodizio-section rodizio-panel hidden" id="tab-rod2">
  <div class="rodizio-header">
    <span class="rodizio-num">2º Rodízio</span>
    <span class="disc-tag disc-ped">PED A4</span>
    <span class="rodizio-title">Pediatria — Simulação, UTIP, Doenças Crônicas, Sala Vermelha</span>
    <span class="rodizio-dates">10 Ago → 30 Ago 2026 · SEM 5–7</span>
  </div>
  <div class="week-tables-group">

  <!-- SEM 05 -->
  <div class="cross-table-wrap type-ped">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="7">SEM 05 &nbsp;·&nbsp; 10–15/08</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 05 como concluída"><input type="checkbox" class="week-done-toggle" data-week="05"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 10/08</th><th>Ter 11/08</th><th>Qua 12/08</th><th>Qui 13/08</th><th>Sex 14/08</th><th>Sáb 15/08</th><th>Dom 16/08</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="act-name">MARCOS</span><span class="act-sub">Simulação</span><span class="loc-chip loc-ped">UNIT</span></td>
        <td class="data-cell"><span class="act-name">LAERTE</span><span class="act-sub">UTIP (metade)</span><span class="loc-chip loc-ped">HUSE</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">ELAINE</span><span class="act-sub">Doenças Crônicas</span><span class="loc-chip loc-ped">AMB — Complexo UNIT</span></td>
        <td class="data-cell"><span class="act-name">RAUL</span><span class="act-sub">Sala Vermelha 15×15 (metade)</span><span class="loc-chip loc-ped">HUSE</span><br><span class="act-name" style="margin-top:4px;display:block">FLÁVIA SP</span><span class="act-sub">Metade da turma (1x/mês)</span><span class="loc-chip loc-ped">MNSL</span></td>
        <td class="data-cell"><span class="act-name">FLÁVIA SP</span><span class="act-sub">Metade da turma (1x/mês)</span><span class="loc-chip loc-ped">MNSL</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="cell-free">A confirmar supervisor</span></td>
        <td class="data-cell"><span class="cell-free">A confirmar supervisor</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">TERESA</span><span class="act-sub">Simulação</span><span class="loc-chip loc-ped">UNIT</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">FLÁVIA SP</span><span class="act-sub">Metade da turma (1x/mês)</span><span class="loc-chip loc-ped">MNSL</span></td>
        <td class="data-cell"><span class="act-name">FLÁVIA SP</span><span class="act-sub">Metade da turma (1x/mês)</span><span class="loc-chip loc-ped">MNSL</span></td>
      </tr>
      <tr>
        <td class="row-header turn-night"><span class="turn-emoji">🌙</span><span class="turn-time">19h&nbsp;·&nbsp;24h</span></td>
        <td class="data-cell"><span class="act-name">Conf. · ALINE</span><span class="loc-chip loc-ped">UNIT (15×15)</span></td>
        <td class="data-cell"><span class="act-name">RAUL · Sala Vermelha (metade)</span><span class="loc-chip loc-ped">HUSE</span><br><span class="act-name" style="margin-top:4px;display:block">Conf. · ANA JOVINA</span><span class="loc-chip loc-ped">UNIT (15×15)</span></td>
        <td class="data-cell"><span class="act-name">JOARA · Sala Vermelha (metade)</span><span class="loc-chip loc-ped">HUSE</span></td>
        <td class="data-cell"><span class="cell-free">—</span></td>
        <td class="data-cell"><span class="cell-free">—</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  <!-- SEM 06 -->
  <div class="cross-table-wrap type-ped">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="7">SEM 06 &nbsp;·&nbsp; 17–22/08</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 06 como concluída"><input type="checkbox" class="week-done-toggle" data-week="06"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 17/08</th><th>Ter 18/08</th><th>Qua 19/08</th><th>Qui 20/08</th><th>Sex 21/08</th><th>Sáb 22/08</th><th>Dom 23/08</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="act-name">MARCOS</span><span class="act-sub">Simulação</span><span class="loc-chip loc-ped">UNIT</span></td>
        <td class="data-cell"><span class="act-name">LAERTE</span><span class="act-sub">UTIP (metade)</span><span class="loc-chip loc-ped">HUSE</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">ELAINE</span><span class="act-sub">Doenças Crônicas</span><span class="loc-chip loc-ped">AMB — Complexo UNIT</span></td>
        <td class="data-cell"><span class="act-name">RAUL</span><span class="act-sub">Sala Vermelha 15×15 (metade)</span><span class="loc-chip loc-ped">HUSE</span><br><span class="act-name" style="margin-top:4px;display:block">FLÁVIA SP</span><span class="act-sub">Metade da turma (1x/mês)</span><span class="loc-chip loc-ped">MNSL</span></td>
        <td class="data-cell"><span class="act-name">FLÁVIA SP</span><span class="act-sub">Metade da turma (1x/mês)</span><span class="loc-chip loc-ped">MNSL</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="cell-free">A confirmar supervisor</span></td>
        <td class="data-cell"><span class="cell-free">A confirmar supervisor</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">TERESA</span><span class="act-sub">Simulação</span><span class="loc-chip loc-ped">UNIT</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">FLÁVIA SP</span><span class="act-sub">Metade da turma (1x/mês)</span><span class="loc-chip loc-ped">MNSL</span></td>
        <td class="data-cell"><span class="act-name">FLÁVIA SP</span><span class="act-sub">Metade da turma (1x/mês)</span><span class="loc-chip loc-ped">MNSL</span></td>
      </tr>
      <tr>
        <td class="row-header turn-night"><span class="turn-emoji">🌙</span><span class="turn-time">19h&nbsp;·&nbsp;24h</span></td>
        <td class="data-cell"><span class="act-name">Conf. · ALINE</span><span class="loc-chip loc-ped">UNIT (15×15)</span></td>
        <td class="data-cell"><span class="act-name">RAUL · Sala Vermelha (metade)</span><span class="loc-chip loc-ped">HUSE</span><br><span class="act-name" style="margin-top:4px;display:block">Conf. · ANA JOVINA</span><span class="loc-chip loc-ped">UNIT (15×15)</span></td>
        <td class="data-cell"><span class="act-name">JOARA · Sala Vermelha (metade)</span><span class="loc-chip loc-ped">HUSE</span></td>
        <td class="data-cell"><span class="cell-free">—</span></td>
        <td class="data-cell"><span class="cell-free">—</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  <!-- SEM 07 -->
  <div class="cross-table-wrap type-ped">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="7">SEM 07 &nbsp;·&nbsp; 24–29/08</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 07 como concluída"><input type="checkbox" class="week-done-toggle" data-week="07"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 24/08</th><th>Ter 25/08</th><th>Qua 26/08</th><th>Qui 27/08</th><th>Sex 28/08</th><th>Sáb 29/08</th><th>Dom 30/08</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="act-name">MARCOS</span><span class="act-sub">Simulação</span><span class="loc-chip loc-ped">UNIT</span></td>
        <td class="data-cell"><span class="act-name">LAERTE</span><span class="act-sub">UTIP (metade)</span><span class="loc-chip loc-ped">HUSE</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">ELAINE</span><span class="act-sub">Doenças Crônicas</span><span class="loc-chip loc-ped">AMB — Complexo UNIT</span></td>
        <td class="data-cell"><span class="act-name">RAUL</span><span class="act-sub">Sala Vermelha 15×15 (metade)</span><span class="loc-chip loc-ped">HUSE</span><br><span class="act-name" style="margin-top:4px;display:block">FLÁVIA SP</span><span class="act-sub">Metade da turma (1x/mês)</span><span class="loc-chip loc-ped">MNSL</span></td>
        <td class="data-cell"><span class="act-name">FLÁVIA SP</span><span class="act-sub">Metade da turma (1x/mês)</span><span class="loc-chip loc-ped">MNSL</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="cell-free">A confirmar supervisor</span></td>
        <td class="data-cell"><span class="cell-free">A confirmar supervisor</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">TERESA</span><span class="act-sub">Simulação</span><span class="loc-chip loc-ped">UNIT</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">FLÁVIA SP</span><span class="act-sub">Metade da turma (1x/mês)</span><span class="loc-chip loc-ped">MNSL</span></td>
        <td class="data-cell"><span class="act-name">FLÁVIA SP</span><span class="act-sub">Metade da turma (1x/mês)</span><span class="loc-chip loc-ped">MNSL</span></td>
      </tr>
      <tr>
        <td class="row-header turn-night"><span class="turn-emoji">🌙</span><span class="turn-time">19h&nbsp;·&nbsp;24h</span></td>
        <td class="data-cell"><span class="act-name">Conf. · ALINE</span><span class="loc-chip loc-ped">UNIT (15×15)</span></td>
        <td class="data-cell"><span class="act-name">RAUL · Sala Vermelha (metade)</span><span class="loc-chip loc-ped">HUSE</span><br><span class="act-name" style="margin-top:4px;display:block">Conf. · ANA JOVINA</span><span class="loc-chip loc-ped">UNIT (15×15)</span></td>
        <td class="data-cell"><span class="act-name">JOARA · Sala Vermelha (metade)</span><span class="loc-chip loc-ped">HUSE</span></td>
        <td class="data-cell"><span class="cell-free">—</span></td>
        <td class="data-cell"><span class="cell-free">—</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  </div><!-- end week-tables-group -->
</section>

<!-- ════════════ 3º RODÍZIO — PSF 10 — SEM 8–11 ════════════ -->
<section class="rodizio-section rodizio-panel hidden" id="tab-rod34">
  <div class="rodizio-header">
    <span class="rodizio-num">3º e 4º Rodízio</span>
    <span class="disc-tag disc-psf10">PSF 10</span>
    <span class="rodizio-title">PSF 10 — UBS Santa Terezinha (Robalo) · MARCOS SUZUKI</span>
    <span class="rodizio-dates">31 Ago → 18 Out 2026 · SEM 8–14</span>
  </div>
  <div class="week-tables-group">

  <!-- SEM 08 -->
  <div class="cross-table-wrap type-psf10">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="6">SEM 08 &nbsp;·&nbsp; 31/08–05/09</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 08 como concluída"><input type="checkbox" class="week-done-toggle" data-week="08"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 31/08</th><th>Ter 01/09</th><th>Qua 02/09</th><th>Qui 03/09</th><th>Sex 04/09</th><th>Sáb 05/09</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">PSF RURAL · LAÍS BATISTA</span><span class="loc-chip loc-psf10">UBS Gabriel Alves da Paixão</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  <!-- SEM 09 -->
  <div class="cross-table-wrap type-psf10">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="6">SEM 09 &nbsp;·&nbsp; 07–12/09</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 09 como concluída"><input type="checkbox" class="week-done-toggle" data-week="09"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 07/09</th><th>Ter 08/09</th><th>Qua 09/09</th><th>Qui 10/09</th><th>Sex 11/09</th><th>Sáb 12/09</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">PSF RURAL · LAÍS BATISTA</span><span class="loc-chip loc-psf10">UBS Gabriel Alves da Paixão</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  <!-- SEM 10 -->
  <div class="cross-table-wrap type-psf10">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="6">SEM 10 &nbsp;·&nbsp; 14–19/09</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 10 como concluída"><input type="checkbox" class="week-done-toggle" data-week="10"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 14/09</th><th>Ter 15/09</th><th>Qua 16/09</th><th>Qui 17/09</th><th>Sex 18/09</th><th>Sáb 19/09</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">PSF RURAL · LAÍS BATISTA</span><span class="loc-chip loc-psf10">UBS Gabriel Alves da Paixão</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  <!-- SEM 11 -->
  <div class="cross-table-wrap type-psf10">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="6">SEM 11 &nbsp;·&nbsp; 21–26/09</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 11 como concluída"><input type="checkbox" class="week-done-toggle" data-week="11"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 21/09</th><th>Ter 22/09</th><th>Qua 23/09</th><th>Qui 24/09</th><th>Sex 25/09</th><th>Sáb 26/09</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">PSF RURAL · LAÍS BATISTA</span><span class="loc-chip loc-psf10">UBS Gabriel Alves da Paixão</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  <!-- SEM 12 -->
  <div class="cross-table-wrap type-psf10">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="6">SEM 12 &nbsp;·&nbsp; 28/09–03/10</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 12 como concluída"><input type="checkbox" class="week-done-toggle" data-week="12"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 28/09</th><th>Ter 29/09</th><th>Qua 30/09</th><th>Qui 01/10</th><th>Sex 02/10</th><th>Sáb 03/10</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">PSF RURAL · LAÍS BATISTA</span><span class="loc-chip loc-psf10">UBS Gabriel Alves da Paixão</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  <!-- SEM 13 -->
  <div class="cross-table-wrap type-psf10">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="6">SEM 13 &nbsp;·&nbsp; 05–10/10</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 13 como concluída"><input type="checkbox" class="week-done-toggle" data-week="13"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 05/10</th><th>Ter 06/10</th><th>Qua 07/10</th><th>Qui 08/10</th><th>Sex 09/10</th><th>Sáb 10/10</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">PSF RURAL · LAÍS BATISTA</span><span class="loc-chip loc-psf10">UBS Gabriel Alves da Paixão</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  <!-- SEM 14 -->
  <div class="cross-table-wrap type-psf10">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="6">SEM 14 &nbsp;·&nbsp; 12–17/10</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 14 como concluída"><input type="checkbox" class="week-done-toggle" data-week="14"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 12/10</th><th>Ter 13/10</th><th>Qua 14/10</th><th>Qui 15/10</th><th>Sex 16/10</th><th>Sáb 17/10</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">PSF RURAL · LAÍS BATISTA</span><span class="loc-chip loc-psf10">UBS Gabriel Alves da Paixão</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="act-name">MARCOS SUZUKI</span><span class="loc-chip loc-psf10">UBS Santa Terezinha — Robalo</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  </div><!-- end week-tables-group -->
</section>

<!-- ════════════ 5º RODÍZIO — PSF 2 — SEM 15–18 ════════════ -->
<section class="rodizio-section rodizio-panel hidden" id="tab-rod56">
  <div class="rodizio-header">
    <span class="rodizio-num">5º e 6º Rodízio</span>
    <span class="disc-tag disc-psf2">PSF 2</span>
    <span class="rodizio-title">PSF 2 — UBS Hugo Gurgel (Coroa do Meio) · SAUL VIEIRA</span>
    <span class="rodizio-dates">19 Out → 06 Dez 2026 · SEM 15–21</span>
  </div>
  <div class="week-tables-group">

  <!-- SEM 15 -->
  <div class="cross-table-wrap type-psf2">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="6">SEM 15 &nbsp;·&nbsp; 19–24/10</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 15 como concluída"><input type="checkbox" class="week-done-toggle" data-week="15"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 19/10</th><th>Ter 20/10</th><th>Qua 21/10</th><th>Qui 22/10</th><th>Sex 23/10</th><th>Sáb 24/10</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (segunda)</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (quinta)</span></td>
        <td class="data-cell"><span class="act-name">PSF RURAL · IGOR</span><span class="loc-chip loc-psf2">UBS Ten. Walter José — Socorro</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (sexta)</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  <!-- SEM 16 -->
  <div class="cross-table-wrap type-psf2">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="6">SEM 16 &nbsp;·&nbsp; 26–31/10</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 16 como concluída"><input type="checkbox" class="week-done-toggle" data-week="16"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 26/10</th><th>Ter 27/10</th><th>Qua 28/10</th><th>Qui 29/10</th><th>Sex 30/10</th><th>Sáb 31/10</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (segunda)</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (quinta)</span></td>
        <td class="data-cell"><span class="act-name">PSF RURAL · IGOR</span><span class="loc-chip loc-psf2">UBS Ten. Walter José — Socorro</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (sexta)</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  <!-- SEM 17 -->
  <div class="cross-table-wrap type-psf2">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="6">SEM 17 &nbsp;·&nbsp; 02–07/11</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 17 como concluída"><input type="checkbox" class="week-done-toggle" data-week="17"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 02/11</th><th>Ter 03/11</th><th>Qua 04/11</th><th>Qui 05/11</th><th>Sex 06/11</th><th>Sáb 07/11</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (segunda)</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (quinta)</span></td>
        <td class="data-cell"><span class="act-name">PSF RURAL · IGOR</span><span class="loc-chip loc-psf2">UBS Ten. Walter José — Socorro</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (sexta)</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  <!-- SEM 18 -->
  <div class="cross-table-wrap type-psf2">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="6">SEM 18 &nbsp;·&nbsp; 09–14/11</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 18 como concluída"><input type="checkbox" class="week-done-toggle" data-week="18"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 09/11</th><th>Ter 10/11</th><th>Qua 11/11</th><th>Qui 12/11</th><th>Sex 13/11</th><th>Sáb 14/11</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (segunda)</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (quinta)</span></td>
        <td class="data-cell"><span class="act-name">PSF RURAL · IGOR</span><span class="loc-chip loc-psf2">UBS Ten. Walter José — Socorro</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (sexta)</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  <!-- SEM 19 -->
  <div class="cross-table-wrap type-psf2">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="6">SEM 19 &nbsp;·&nbsp; 16–21/11</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 19 como concluída"><input type="checkbox" class="week-done-toggle" data-week="19"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 16/11</th><th>Ter 17/11</th><th>Qua 18/11</th><th>Qui 19/11</th><th>Sex 20/11</th><th>Sáb 21/11</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (segunda)</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (quinta)</span></td>
        <td class="data-cell"><span class="act-name">PSF RURAL · IGOR</span><span class="loc-chip loc-psf2">UBS Ten. Walter José — Socorro</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (sexta)</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  <!-- SEM 20 -->
  <div class="cross-table-wrap type-psf2">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="6">SEM 20 &nbsp;·&nbsp; 23–28/11</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 20 como concluída"><input type="checkbox" class="week-done-toggle" data-week="20"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 23/11</th><th>Ter 24/11</th><th>Qua 25/11</th><th>Qui 26/11</th><th>Sex 27/11</th><th>Sáb 28/11</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (segunda)</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (quinta)</span></td>
        <td class="data-cell"><span class="act-name">PSF RURAL · IGOR</span><span class="loc-chip loc-psf2">UBS Ten. Walter José — Socorro</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (sexta)</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  <!-- SEM 21 -->
  <div class="cross-table-wrap type-psf2">
  <table class="cross-table">
    <colgroup><col class="col-turno"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"><col class="col-day"></colgroup>
    <thead>
      <tr><th>Turno / Dia</th><th class="week-th" colspan="6">SEM 21 &nbsp;·&nbsp; 30/11–05/12 ✦ FIM</th></tr>
      <tr class="day-header-row"><th class="week-switch-cell"><label class="week-switch" title="Marcar SEM 21 como concluída"><input type="checkbox" class="week-done-toggle" data-week="21"><span class="week-switch-track"></span><span class="week-switch-icon">✓</span></label></th><th>Seg 30/11</th><th>Ter 01/12</th><th>Qua 02/12</th><th>Qui 03/12</th><th>Sex 04/12</th><th>Sáb 05/12</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="row-header turn-morning"><span class="turn-emoji">☀️</span><span class="turn-time">07h&nbsp;·&nbsp;12h</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (segunda)</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (quinta)</span></td>
        <td class="data-cell"><span class="act-name">PSF RURAL · IGOR</span><span class="loc-chip loc-psf2">UBS Ten. Walter José — Socorro</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">Fim do 9º Período</span></td>
      </tr>
      <tr>
        <td class="row-header turn-afternoon"><span class="turn-emoji">🌤</span><span class="turn-time">13h&nbsp;·&nbsp;18h</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="act-name">SAUL VIEIRA</span><span class="loc-chip loc-psf2">UBS Hugo Gurgel — Coroa do Meio</span></td>
        <td class="data-cell"><span class="cell-free">Sem atividade (sexta)</span></td>
        <td class="data-cell cell-empty"><span class="cell-free">—</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  </div><!-- end week-tables-group -->
</section>

<!-- FOOTER -->
<footer class="page-footer">
  <p>Fonte: PSF.csv · NOSSA_TURMA.csv · PEDIATRIA.csv &nbsp;·&nbsp; Grupo 09-14 · 9ª Etapa · 2026.2</p>
  <p style="margin-top:0.4rem;opacity:0.65;">As conferências UNIT seguem programação do supervisor · PSF Rural/Quarta segue escala de LAÍS BATISTA (PSF 10) e IGOR (PSF 2)</p>
</footer>

</div>

<script>
  const toggle = document.getElementById('themeToggle');
  const html = document.documentElement;

  // Restore preference
  const saved = localStorage.getItem('theme') || 'dark';
  html.setAttribute('data-theme', saved);
  toggle.checked = (saved === 'light');

  toggle.addEventListener('change', () => {
    const theme = toggle.checked ? 'light' : 'dark';
    html.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
  });

  // ─── Seletor de rodízios (tabs com indicador deslizante) ───
  (function(){
    const nav = document.getElementById('rodizioTabs');
    const indicator = document.getElementById('tabIndicator');
    const buttons = Array.from(nav.querySelectorAll('.rodizio-tab-btn'));
    const panels = Array.from(document.querySelectorAll('.rodizio-panel'));

    function moveIndicatorTo(btn, animate){
      const navRect = nav.getBoundingClientRect();
      const btnRect = btn.getBoundingClientRect();
      if(!animate){ indicator.style.transition = 'none'; }
      indicator.style.width = btnRect.width + 'px';
      indicator.style.transform = 'translateX(' + (btnRect.left - navRect.left - 0) + 'px)';
      indicator.style.background = 'var(--tab-' + btn.dataset.color + ')';
      if(!animate){
        requestAnimationFrame(() => { indicator.style.transition = ''; });
      }
    }

    function selectTab(btn){
      buttons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      panels.forEach(p => p.classList.add('hidden'));
      const target = document.getElementById(btn.dataset.target);
      if(target) target.classList.remove('hidden');
      moveIndicatorTo(btn, true);
    }

    buttons.forEach(btn => {
      btn.addEventListener('click', () => selectTab(btn));
    });

    // Posiciona o indicador imediatamente e novamente após o load completo
    // (garante posição correta mesmo com troca de fontes/web fonts)
    const initialActive = nav.querySelector('.rodizio-tab-btn.active') || buttons[0];
    moveIndicatorTo(initialActive, false);

    window.addEventListener('load', () => {
      const active = nav.querySelector('.rodizio-tab-btn.active') || buttons[0];
      moveIndicatorTo(active, false);
    });

    // Reposiciona ao redimensionar a janela (sem animação)
    let resizeTimeout;
    window.addEventListener('resize', () => {
      clearTimeout(resizeTimeout);
      resizeTimeout = setTimeout(() => {
        const active = nav.querySelector('.rodizio-tab-btn.active') || buttons[0];
        moveIndicatorTo(active, false);
      }, 100);
    });
  })();

  // ─── Destaque do dia de hoje (SIMULADO: Qua 15/07) ───
  // Quando isto virar app Streamlit, este valor passa a vir da data real do servidor.
  (function(){
    const today = new Date();
    const todayStr = String(today.getDate()).padStart(2, '0') + '/' + String(today.getMonth() + 1).padStart(2, '0');

    document.querySelectorAll('.cross-table').forEach(table => {
      const headerRow = table.querySelector('.day-header-row');
      if(!headerRow) return;
      const ths = Array.from(headerRow.children);
      ths.forEach((th, idx) => {
        if(idx === 0) return; // primeira coluna = "Turno / Dia"
        const text = th.textContent.trim();       // ex: "Qua 15/07"
        const datePart = text.split(/\s+/).pop();  // "15/07"
        if(datePart === todayStr){
          th.classList.add('today-col');
          const rows = table.querySelectorAll('tbody tr');
          rows.forEach(row => {
            const cell = row.children[idx];
            if(cell && cell.classList.contains('data-cell')){
              cell.classList.add('today-col');
            }
          });
        }
      });
    });
  })();

  // ─── Seletor de usuário + memória individual do progresso semanal ───
  (function(){
    const USER_KEY = 'internato_gabriel_current_user';
    const userRow = document.getElementById('userSelectRow');
    if(!userRow) return;
    const userButtons = Array.from(userRow.querySelectorAll('.user-badge'));
    const toggles = Array.from(document.querySelectorAll('.week-done-toggle'));
    const pageTitleEl = document.getElementById('pageTitle');

    function storageKey(user, week){
      return 'internato_gabriel_week_done_' + user + '_' + week;
    }
    function getCurrentUser(){
      return localStorage.getItem(USER_KEY) || 'Gabriel';
    }
    function setCurrentUser(u){
      localStorage.setItem(USER_KEY, u);
    }
    function applyUserState(user){
      userButtons.forEach(b => b.classList.toggle('active', b.dataset.user === user));
      const activeBtn = userButtons.find(b => b.dataset.user === user);
      const fullName = activeBtn ? activeBtn.dataset.fullname : user;
      if(pageTitleEl && fullName) pageTitleEl.textContent = fullName;
      if(fullName) document.title = 'Horário Internato — ' + fullName + ' · 9º Período';
      toggles.forEach(t => {
        const week = t.dataset.week;
        const done = localStorage.getItem(storageKey(user, week)) === '1';
        t.checked = done;
        const wrap = t.closest('.cross-table-wrap');
        if(wrap) wrap.classList.toggle('week-done', done);
      });
    }

    userButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        setCurrentUser(btn.dataset.user);
        applyUserState(btn.dataset.user);
      });
    });

    toggles.forEach(t => {
      t.addEventListener('change', () => {
        const user = getCurrentUser();
        const week = t.dataset.week;
        localStorage.setItem(storageKey(user, week), t.checked ? '1' : '0');
        const wrap = t.closest('.cross-table-wrap');
        if(wrap) wrap.classList.toggle('week-done', t.checked);
      });
    });

    applyUserState(getCurrentUser());
  })();
</script>
</body>
</html>
"""

# Renderizar o HTML ocupando a altura da tela
components.html(html_content, height=1200, scrolling=True)
