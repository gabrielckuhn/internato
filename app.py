import json
import datetime
import streamlit as st

# ══════════════════════════════════════════════════════════════
# DADOS DO HORÁRIO (extraídos fielmente do HTML original)
# ══════════════════════════════════════════════════════════════
DATA_JSON = r'''
__DATA_PLACEHOLDER__
'''

DATA = json.loads(DATA_JSON)

st.set_page_config(
    page_title="Horário Internato — Gabriel Kuhn · 9º Período",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════════════════════
# ESTADO
# ══════════════════════════════════════════════════════════════
if "theme" not in st.session_state:
    st.session_state.theme = "dark"
if "current_user" not in st.session_state:
    st.session_state.current_user = "Gabriel"

def week_done_key(user, week_num):
    return f"week_done_{user}_{week_num}"

# ══════════════════════════════════════════════════════════════
# TEMAS (paleta de cores — igual ao HTML original)
# Alterações pedidas: destaque do dia atual em ROXO com baixa
# transparência; véu de "semana concluída" em tom ESBRANQUIÇADO
# (em vez do véu colorido azul/verde/roxo por rodízio).
# ══════════════════════════════════════════════════════════════
THEMES = {
    "dark": {
        "bg-base": "#14161C",
        "bg-glow-1": "rgba(56,139,253,0.08)",
        "bg-glow-2": "rgba(48,213,136,0.07)",
        "bg-glow-3": "rgba(168,85,247,0.06)",
        "bg-glow-4": "rgba(230,57,70,0.06)",
        "glass-bg": "rgba(20, 22, 28, 0.55)",
        "glass-hover": "rgba(30, 34, 44, 0.78)",
        "glass-border": "rgba(255,255,255,0.10)",
        "glass-shadow": "0 20px 60px -22px rgba(0,0,0,0.55)",
        "text-primary": "rgba(255,255,255,0.95)",
        "text-secondary": "rgba(255,255,255,0.62)",
        "text-tertiary": "rgba(255,255,255,0.35)",
        "divider": "rgba(255,255,255,0.06)",
        "th-bg": "rgba(255,255,255,0.04)",
        "th-text": "rgba(255,255,255,0.38)",
        "th-hover-bg": "rgba(255,255,255,0.14)",
        "th-hover-text": "rgba(255,255,255,0.95)",

        "ped-color": "rgba(56,139,253,0.18)",
        "ped-bg-cell": "rgba(56,139,253,0.11)",
        "ped-border": "rgba(56,139,253,0.45)",
        "ped-text": "#7ab8ff",
        "ped-section-border": "rgba(56,139,253,0.28)",

        "psf10-color": "rgba(48,213,136,0.15)",
        "psf10-bg-cell": "rgba(48,213,136,0.10)",
        "psf10-border": "rgba(48,213,136,0.40)",
        "psf10-text": "#5de8a4",
        "psf10-section-border": "rgba(48,213,136,0.24)",

        "psf2-color": "rgba(168,85,247,0.15)",
        "psf2-bg-cell": "rgba(168,85,247,0.10)",
        "psf2-border": "rgba(168,85,247,0.40)",
        "psf2-text": "#c084fc",
        "psf2-section-border": "rgba(168,85,247,0.24)",

        "turn-morning": "#ffd24e",
        "turn-afternoon": "#7ab8ff",
        "turn-night": "#c084fc",
        "free-color": "rgba(255,255,255,0.28)",
        "loc-bg": "rgba(255,255,255,0.08)",
        "loc-border": "rgba(255,255,255,0.14)",
        "loc-text": "rgba(255,255,255,0.72)",
        "footer-border": "rgba(255,255,255,0.07)",
        "footer-text": "rgba(255,255,255,0.30)",
        "switch-bg": "rgba(255,255,255,0.08)",
        "empty-opacity": "0.40",

        # destaque do dia — ROXO, baixa transparência
        "today-bg": "rgba(168,85,247,0.10)",
        "today-bg-strong": "rgba(168,85,247,0.17)",
        "today-border": "rgba(168,85,247,0.50)",
        "today-text": "#c9a3ff",

        # semana concluída — véu ESBRANQUIÇADO
        "week-done-veil": "rgba(255,255,255,0.14)",
        "week-done-track": "rgba(255,255,255,0.55)",
        "week-done-knob": "#f4f4f6",
        "week-done-opacity": "0.40",
        "week-done-opacity-hover": "0.70",
    },
    "light": {
        "bg-base": "#f0f2f7",
        "bg-glow-1": "rgba(56,139,253,0.10)",
        "bg-glow-2": "rgba(48,213,136,0.09)",
        "bg-glow-3": "rgba(168,85,247,0.08)",
        "bg-glow-4": "rgba(230,57,70,0.07)",
        "glass-bg": "rgba(255,255,255,0.72)",
        "glass-hover": "rgba(255,255,255,0.90)",
        "glass-border": "rgba(0,0,0,0.09)",
        "glass-shadow": "0 8px 32px -10px rgba(0,0,0,0.14)",
        "text-primary": "rgba(15,18,28,0.92)",
        "text-secondary": "rgba(15,18,28,0.60)",
        "text-tertiary": "rgba(15,18,28,0.40)",
        "divider": "rgba(0,0,0,0.07)",
        "th-bg": "rgba(0,0,0,0.04)",
        "th-text": "rgba(0,0,0,0.40)",
        "th-hover-bg": "rgba(0,0,0,0.13)",
        "th-hover-text": "rgba(15,18,28,0.96)",

        "ped-color": "rgba(56,139,253,0.12)",
        "ped-bg-cell": "rgba(56,139,253,0.08)",
        "ped-border": "rgba(56,139,253,0.40)",
        "ped-text": "#1a6ec7",
        "ped-section-border": "rgba(56,139,253,0.30)",

        "psf10-color": "rgba(16,153,90,0.12)",
        "psf10-bg-cell": "rgba(16,153,90,0.08)",
        "psf10-border": "rgba(16,153,90,0.38)",
        "psf10-text": "#0d7a4e",
        "psf10-section-border": "rgba(16,153,90,0.25)",

        "psf2-color": "rgba(130,55,210,0.12)",
        "psf2-bg-cell": "rgba(130,55,210,0.08)",
        "psf2-border": "rgba(130,55,210,0.38)",
        "psf2-text": "#7428c8",
        "psf2-section-border": "rgba(130,55,210,0.25)",

        "turn-morning": "#b5830a",
        "turn-afternoon": "#1a6ec7",
        "turn-night": "#7428c8",
        "free-color": "rgba(0,0,0,0.32)",
        "loc-bg": "rgba(0,0,0,0.05)",
        "loc-border": "rgba(0,0,0,0.12)",
        "loc-text": "rgba(0,0,0,0.60)",
        "footer-border": "rgba(0,0,0,0.10)",
        "footer-text": "rgba(0,0,0,0.38)",
        "switch-bg": "rgba(0,0,0,0.08)",
        "empty-opacity": "0.45",

        # destaque do dia — ROXO, baixa transparência
        "today-bg": "rgba(130,55,210,0.07)",
        "today-bg-strong": "rgba(130,55,210,0.13)",
        "today-border": "rgba(130,55,210,0.45)",
        "today-text": "#7428c8",

        # semana concluída — véu ESBRANQUIÇADO
        "week-done-veil": "rgba(255,255,255,0.55)",
        "week-done-track": "rgba(0,0,0,0.30)",
        "week-done-knob": "#ffffff",
        "week-done-opacity": "0.45",
        "week-done-opacity-hover": "0.75",
    },
}

def build_css(t: dict) -> str:
    return f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {{
  font-family: 'Inter', system-ui, sans-serif;
}}

.stApp {{
  background: {t['bg-base']};
}}
.stApp::before {{
  content:'';
  position:fixed; inset:0;
  background:
    radial-gradient(ellipse 80% 50% at 10% 20%, {t['bg-glow-1']} 0%, transparent 60%),
    radial-gradient(ellipse 60% 40% at 85% 10%, {t['bg-glow-2']} 0%, transparent 55%),
    radial-gradient(ellipse 70% 60% at 50% 90%, {t['bg-glow-3']} 0%, transparent 60%),
    radial-gradient(ellipse 50% 40% at 90% 70%, {t['bg-glow-4']} 0%, transparent 50%);
  z-index:0; pointer-events:none;
}}

.block-container {{ max-width:1180px; padding-top:1.5rem; padding-bottom:3rem; }}

/* ── Header ── */
.page-header{{
  text-align:center; margin-bottom:1.6rem; padding:2.2rem 2rem;
  background:{t['glass-bg']}; backdrop-filter:blur(30px) saturate(180%);
  -webkit-backdrop-filter:blur(30px) saturate(180%);
  border-radius:1.25rem; box-shadow:{t['glass-shadow']};
  border:0.5px solid {t['glass-border']};
  position:relative; overflow:hidden;
}}
.page-header::after{{
  content:''; position:absolute; top:-60px; right:-60px;
  width:200px; height:200px;
  background:radial-gradient(circle, rgba(168,85,247,0.13) 0%, transparent 70%);
  border-radius:50%; pointer-events:none;
}}
.eyebrow{{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.18em;
  text-transform:uppercase;color:{t['text-secondary']};margin-bottom:.6rem;}}
.page-title{{font-size:clamp(1.6rem,4vw,2.4rem);font-weight:700;
  background:linear-gradient(135deg,{t['text-primary']} 0%,{t['text-secondary']} 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  line-height:1.2;margin-bottom:.4rem;}}
.page-subtitle{{font-size:13px;color:{t['text-secondary']};letter-spacing:.03em;}}
.badge-row{{display:flex;justify-content:center;gap:.6rem;flex-wrap:wrap;margin-top:1.1rem;}}
.badge{{display:inline-flex;align-items:center;gap:.4rem;padding:.28rem .85rem;border-radius:100px;
  font-size:11.5px;font-weight:500;letter-spacing:.04em;border:.5px solid;}}
.badge-ped{{background:{t['ped-color']};border-color:{t['ped-border']};color:{t['ped-text']};}}
.badge-psf10{{background:{t['psf10-color']};border-color:{t['psf10-border']};color:{t['psf10-text']};}}
.badge-psf2{{background:{t['psf2-color']};border-color:{t['psf2-border']};color:{t['psf2-text']};}}
.dot{{width:6px;height:6px;border-radius:50%;display:inline-block;}}
.dot-ped{{background:#388bfd;}} .dot-psf10{{background:#30d588;}} .dot-psf2{{background:#a855f7;}}

.user-select-label{{
  font-family:'JetBrains Mono',monospace;font-size:10.5px;letter-spacing:.08em;
  text-transform:uppercase;color:{t['text-tertiary']};
}}

/* ── Rodízio header bar ── */
.rodizio-header{{
  display:flex;align-items:center;gap:.8rem 1rem;margin-bottom:1.1rem;
  padding:.9rem 1.3rem;background:{t['glass-bg']};
  backdrop-filter:blur(30px) saturate(180%); -webkit-backdrop-filter:blur(30px) saturate(180%);
  border-radius:.9rem; box-shadow:{t['glass-shadow']}; border:.5px solid {t['glass-border']};
  flex-wrap:wrap;
}}
.rodizio-num{{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.12em;
  color:{t['text-secondary']};text-transform:uppercase;white-space:nowrap;}}
.rodizio-title{{font-size:1rem;font-weight:600;color:{t['text-primary']};}}
.rodizio-dates{{font-family:'JetBrains Mono',monospace;font-size:11.5px;color:{t['text-secondary']};
  margin-left:auto;white-space:nowrap;}}
.disc-tag{{padding:.22rem .7rem;border-radius:100px;font-size:11px;font-weight:600;
  letter-spacing:.06em;text-transform:uppercase;border:.5px solid;}}
.disc-ped{{background:{t['ped-color']};border-color:{t['ped-border']};color:{t['ped-text']};}}
.disc-psf10{{background:{t['psf10-color']};border-color:{t['psf10-border']};color:{t['psf10-text']};}}
.disc-psf2{{background:{t['psf2-color']};border-color:{t['psf2-border']};color:{t['psf2-text']};}}

/* ── Week card / cross-table ── */
.week-toolbar{{display:flex;align-items:center;justify-content:space-between;
  margin:0 0 -0.1rem 0;}}
.week-label-txt{{font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:600;
  letter-spacing:.08em;color:{t['text-secondary']};}}

.cross-table-wrap{{
  background:{t['glass-bg']}; backdrop-filter:blur(30px) saturate(180%);
  -webkit-backdrop-filter:blur(30px) saturate(180%);
  border-radius:1.1rem; box-shadow:{t['glass-shadow']};
  border:.5px solid {t['glass-border']}; overflow:hidden; position:relative;
  margin-bottom:.9rem; transition:opacity .35s ease;
}}
.cross-table-wrap.type-ped{{border-color:{t['ped-section-border']};}}
.cross-table-wrap.type-psf10{{border-color:{t['psf10-section-border']};}}
.cross-table-wrap.type-psf2{{border-color:{t['psf2-section-border']};}}
.cross-table-wrap.week-done{{opacity:{t['week-done-opacity']};}}
.cross-table-wrap.week-done::after{{
  content:''; position:absolute; inset:0; border-radius:inherit;
  pointer-events:none; z-index:3; background:{t['week-done-veil']};
}}

.cross-table{{width:100%;border-collapse:collapse;table-layout:fixed;}}
.cross-table col.col-turno{{width:130px;}}
.cross-table col.col-day{{width:calc((100% - 130px) / 6);}}

.cross-table thead tr th{{
  background:{t['th-bg']}; padding:.6rem .9rem; text-align:center;
  font-size:10.5px;font-weight:600;letter-spacing:.09em;text-transform:uppercase;
  color:{t['th-text']}; border-bottom:.5px solid {t['divider']}; white-space:nowrap;
}}
.cross-table thead tr th:first-child{{text-align:left;border-right:.5px solid {t['divider']};padding-left:1.1rem;}}

.cross-table .day-header-row th{{
  background:{t['th-bg']}; padding:.28rem .9rem;
  font-family:'JetBrains Mono',monospace; font-size:10px;font-weight:500;
  color:{t['text-tertiary']}; border-bottom:.5px solid {t['divider']};
  text-align:center; letter-spacing:.06em;
}}
.cross-table .day-header-row th:first-child{{border-right:.5px solid {t['divider']};padding-left:1.1rem;text-align:left;}}

.cross-table .day-header-row th.today-col{{
  background:{t['today-bg-strong']} !important; color:{t['today-text']} !important;
  font-weight:700;
  box-shadow:inset 1px 0 0 0 {t['today-border']}, inset -1px 0 0 0 {t['today-border']}, inset 0 -2px 0 0 {t['today-border']};
}}
.cross-table tbody tr td.data-cell.today-col{{
  background:{t['today-bg']} !important;
  box-shadow:inset 1px 0 0 0 {t['today-border']}, inset -1px 0 0 0 {t['today-border']};
}}

.cross-table tbody tr td.row-header{{
  font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:600;
  padding:.7rem .8rem .7rem 1.05rem; white-space:nowrap;
  border-right:.5px solid {t['divider']}; border-bottom:.5px solid {t['divider']};
  vertical-align:middle; background:{t['th-bg']};
}}
.turn-emoji{{font-size:15px;line-height:1;vertical-align:middle;margin-right:.3em;display:inline-block;}}
.turn-time{{font-size:12.5px;font-weight:600;letter-spacing:.01em;vertical-align:middle;}}
.row-header.turn-morning{{color:{t['turn-morning']};}}
.row-header.turn-afternoon{{color:{t['turn-afternoon']};}}
.row-header.turn-night{{color:{t['turn-night']};}}

.cross-table tbody tr td.data-cell{{
  padding:.68rem .8rem; vertical-align:top;
  border-bottom:.5px solid {t['divider']}; border-right:.5px solid {t['divider']};
  font-size:12.5px;
}}
.cross-table tbody tr td.data-cell:last-child{{border-right:none;}}
.cross-table tbody tr:last-child td{{border-bottom:none;}}

.cell-free{{font-size:11px;color:{t['free-color']};font-style:italic;}}
.cell-empty{{opacity:{t['empty-opacity']};}}
.act-name{{color:{t['text-primary']};font-weight:600;font-size:12px;display:block;line-height:1.35;}}
.act-sub{{color:{t['text-secondary']};font-size:11.5px;display:block;}}
.act-block + .act-block{{margin-top:.4rem;}}

.loc-chip{{
  display:inline-block;margin-top:.3rem;padding:.16rem .5rem;border-radius:5px;
  font-size:10px;font-weight:600;letter-spacing:.04em;
  background:{t['loc-bg']};border:.5px solid {t['loc-border']};color:{t['loc-text']};
  line-height:1.4;
}}
.loc-ped{{background:{t['ped-bg-cell']};border-color:{t['ped-border']};color:{t['ped-text']};}}
.loc-psf10{{background:{t['psf10-bg-cell']};border-color:{t['psf10-border']};color:{t['psf10-text']};}}
.loc-psf2{{background:{t['psf2-bg-cell']};border-color:{t['psf2-border']};color:{t['psf2-text']};}}

/* ── Footer ── */
.page-footer{{
  text-align:center;margin-top:2.2rem;padding-top:1.4rem;
  border-top:.5px solid {t['footer-border']}; color:{t['footer-text']};
  font-size:11px;font-family:'JetBrains Mono',monospace;letter-spacing:.06em;
}}

/* ── Streamlit widget re-skin ── */
div[data-testid="stCheckbox"] label span{{font-size:12px;}}
div[data-baseweb="tab-list"]{{gap:4px;}}
button[data-baseweb="tab"]{{font-family:'Inter',sans-serif;}}

/* Segmented / radio user badges */
div[role="radiogroup"] label{{
  border:.5px solid {t['glass-border']}; border-radius:100px; padding:.15rem .8rem;
  background:{t['glass-bg']};
}}
</style>
"""

# ══════════════════════════════════════════════════════════════
# HELPERS DE RENDERIZAÇÃO
# ══════════════════════════════════════════════════════════════
DAY_ABBR = {0: "Seg", 1: "Ter", 2: "Qua", 3: "Qui", 4: "Sex", 5: "Sáb", 6: "Dom"}


def get_today_ddmm():
    """Retorna a data de hoje no formato dd/mm (2026), para casar
    com os cabeçalhos de dia das tabelas (que também usam dd/mm)."""
    today = datetime.date.today()
    return f"{today.day:02d}/{today.month:02d}"


def render_cell_html(cell: dict) -> str:
    parts = []
    for item in cell["items"]:
        if "free" in item:
            parts.append(f'<span class="cell-free">{item["free"]}</span>')
        else:
            block = [f'<span class="act-name">{item.get("name","")}</span>']
            if item.get("sub"):
                block.append(f'<span class="act-sub">{item["sub"]}</span>')
            if item.get("detail"):
                block.append(f'<span class="act-detail">{item["detail"]}</span>')
            if item.get("loc"):
                loc_type = item.get("loc_type") or ""
                block.append(f'<span class="loc-chip loc-{loc_type}">{item["loc"]}</span>')
            parts.append(f'<span class="act-block">{"".join(block)}</span>')
    return "".join(parts)


def render_week_table(week: dict, today_ddmm: str) -> str:
    days = week["days"]  # ex: ["Seg 13/07", ...]
    today_idx = None
    for i, d in enumerate(days):
        date_part = d.strip().split()[-1]
        if date_part == today_ddmm:
            today_idx = i
            break

    # cabeçalho semana
    thead = f'<tr><th>Turno / Dia</th><th colspan="6">{week["week_label"].replace(chr(160)," ")}</th></tr>'
    day_ths = []
    for i, d in enumerate(days):
        cls = ' class="today-col"' if i == today_idx else ""
        day_ths.append(f"<th{cls}>{d}</th>")
    thead += f'<tr class="day-header-row"><th></th>{"".join(day_ths)}</tr>'

    # corpo
    rows_html = []
    for shift in week["shifts"]:
        cells_html = []
        for i, cell in enumerate(shift["cells"]):
            cls = "data-cell"
            if cell.get("empty"):
                cls += " cell-empty"
            if i == today_idx:
                cls += " today-col"
            cells_html.append(f'<td class="{cls}">{render_cell_html(cell)}</td>')
        row = (
            f'<tr><td class="row-header {shift["turn_class"]}">'
            f'<span class="turn-emoji">{shift["emoji"]}</span>'
            f'<span class="turn-time">{shift["time_label"]}</span></td>'
            f'{"".join(cells_html)}</tr>'
        )
        rows_html.append(row)

    table_html = (
        f'<table class="cross-table">'
        f'<colgroup><col class="col-turno">{"<col class=" + chr(34) + "col-day" + chr(34) + ">" * 6}</colgroup>'
        f'<thead>{thead}</thead><tbody>{"".join(rows_html)}</tbody></table>'
    )
    return table_html


def render_week(week: dict, wtype: str, today_ddmm: str, user: str):
    key = week_done_key(user, week["week_num"])
    done = st.session_state.get(key, False)

    col_a, col_b = st.columns([5, 1])
    with col_a:
        st.markdown(
            f'<div class="week-label-txt">{week["week_label"].replace(chr(160), " ")}</div>',
            unsafe_allow_html=True,
        )
    with col_b:
        done = st.checkbox(
            "Concluída ✓",
            value=done,
            key=key,
            label_visibility="visible",
        )

    wrap_class = f"cross-table-wrap type-{wtype}" + (" week-done" if done else "")
    table_html = render_week_table(week, today_ddmm)
    st.markdown(f'<div class="{wrap_class}">{table_html}</div>', unsafe_allow_html=True)


def render_panel(panel: dict, today_ddmm: str, user: str):
    disc = panel["disc_type"]
    st.markdown(
        f'''<div class="rodizio-header">
            <span class="rodizio-num">{panel["rodizio_num"]}</span>
            <span class="disc-tag disc-{disc}">{panel["disc_text"]}</span>
            <span class="rodizio-title">{panel["rodizio_title"]}</span>
            <span class="rodizio-dates">{panel["rodizio_dates"]}</span>
        </div>''',
        unsafe_allow_html=True,
    )
    for week in panel["weeks"]:
        render_week(week, panel["disc_type"], today_ddmm, user)

  # ══════════════════════════════════════════════════════════════
# BARRA SUPERIOR — tema + usuário
# ══════════════════════════════════════════════════════════════
top_l, top_r = st.columns([3, 2])
with top_r:
    c1, c2 = st.columns([3, 1])
    with c1:
        user_labels = [u["label"] for u in DATA["user_badges"]]
        user_default_idx = user_labels.index(st.session_state.current_user) if st.session_state.current_user in user_labels else 0
        chosen_label = st.radio(
            "Progresso de:",
            user_labels,
            index=user_default_idx,
            horizontal=True,
            key="user_radio",
            label_visibility="visible",
        )
        st.session_state.current_user = chosen_label
    with c2:
        theme_choice = st.radio(
            "Tema",
            ["🌙 Escuro", "☀️ Claro"],
            index=0 if st.session_state.theme == "dark" else 1,
            key="theme_radio",
            label_visibility="visible",
        )
        st.session_state.theme = "dark" if "Escuro" in theme_choice else "light"

THEME = THEMES[st.session_state.theme]
st.markdown(build_css(THEME), unsafe_allow_html=True)

current_user = st.session_state.current_user
fullname = next(
    (u["fullname"] for u in DATA["user_badges"] if u["label"] == current_user),
    DATA["page_title"],
)

# ══════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════
badges_html = "".join(
    f'<span class="badge badge-{b["type"]}"><span class="dot dot-{b["type"]}"></span> {b["text"]}</span>'
    for b in DATA["badges"]
)

st.markdown(
    f'''<div class="page-header">
        <p class="eyebrow">{DATA["eyebrow"]}</p>
        <h1 class="page-title">{fullname}</h1>
        <p class="page-subtitle">{DATA["page_subtitle_html"]}</p>
        <div class="badge-row">{badges_html}</div>
    </div>''',
    unsafe_allow_html=True,
)

# ══════════════════════════════════════════════════════════════
# ABAS DE RODÍZIO
# ══════════════════════════════════════════════════════════════
today_ddmm = get_today_ddmm()

tab_labels = [f'{t["eyebrow"]} · {t["title"]}' for t in DATA["tabs"]]
st_tabs = st.tabs(tab_labels)

for st_tab, panel in zip(st_tabs, DATA["panels"]):
    with st_tab:
        render_panel(panel, today_ddmm, current_user)

# ══════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════
footer_html = "".join(f"<p>{line}</p>" for line in DATA["footer_lines"])
st.markdown(f'<div class="page-footer">{footer_html}</div>', unsafe_allow_html=True)
