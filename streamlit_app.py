import streamlit as st
import streamlit.components.v1 as components

# 1. Main Application Header
st.title("VA Calculator")
st.subheader("Standard Calculator")

# 2. Initialize Session States
if "expression" not in st.session_state:
    st.session_state.expression = ""
if "show_secret" not in st.session_state:
    st.session_state.show_secret = False

# Helper Functions to manipulate display expression
def append_to_expression(char):
    st.session_state.expression += str(char)

def clear_expression():
    st.session_state.expression = ""

def evaluate_expression():
    try:
        expr = st.session_state.expression.replace("×", "*").replace("÷", "/")
        if expr:
            result = eval(expr, {"__builtins__": None}, {})
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            st.session_state.expression = str(result)
    except ZeroDivisionError:
        st.error("Cannot divide by zero!")
        st.session_state.expression = ""
    except Exception:
        st.error("Invalid Expression")
        st.session_state.expression = ""

# 3. Hidden Keyboard Input & Visual Display Screen
# This text input captures physical keyboard events globally and syncs it with session state
kb_input = st.text_input(
    "Keyboard Entry Link", 
    value=st.session_state.expression, 
    label_visibility="collapsed", 
    key="hidden_kb_sync"
)

# Update state if keyboard text input changes manually
if kb_input != st.session_state.expression:
    st.session_state.expression = kb_input
    st.rerun()

st.markdown(
    f"""
    <div style="
        background-color: #f0f2f6; 
        padding: 20px; 
        border-radius: 10px; 
        font-size: 2.2rem; 
        text-align: right; 
        font-family: monospace; 
        margin-bottom: 20px;
        min-height: 80px;
        border: 1px solid #dcdfe6;
        color: #333333;
    ">
        {st.session_state.expression if st.session_state.expression else "0"}
    </div>
    
    <script>
    // JavaScript listener to route keyboard strokes straight to Streamlit's input framework
    document.addEventListener('keydown', function(e) {{
        const inputs = parent.document.querySelectorAll('input[type="text"]');
        if (inputs.length > 0) {{
            const targetInput = inputs[0];
            if (parent.document.activeElement !== targetInput) {{
                targetInput.focus();
            }}
        }}
    }});
    </script>
    """,
    unsafe_allow_html=True,
)

# 4. Calculator Button Grid Layout
r1_c1, r1_c2, r1_c3, r1_c4 = st.columns(4)
r2_c1, r2_c2, r2_c3, r2_c4 = st.columns(4)
r3_c1, r3_c2, r3_c3, r3_c4 = st.columns(4)
r4_c1, r4_c2, r4_c3, r4_c4 = st.columns(4)
r5_c1, r5_c2, r5_c3 = st.columns(3)

# --- Row 1 ---
if r1_c1.button("C", use_container_width=True):
    clear_expression()
    st.rerun()
if r1_c2.button("(", use_container_width=True):
    append_to_expression("(")
    st.rerun()
if r1_c3.button(")", use_container_width=True):
    append_to_expression(")")
    st.rerun()
if r1_c4.button("÷", use_container_width=True):
    append_to_expression("÷")
    st.rerun()

# --- Row 2 ---
if r2_c1.button("7", use_container_width=True):
    append_to_expression(7)
    st.rerun()
if r2_c2.button("8", use_container_width=True):
    append_to_expression(8)
    st.rerun()
if r2_c3.button("9", use_container_width=True):
    append_to_expression(9)
    st.rerun()
if r2_c4.button("×", use_container_width=True):
    append_to_expression("×")
    st.rerun()

# --- Row 3 ---
if r3_c1.button("4", use_container_width=True):
    append_to_expression(4)
    st.rerun()
if r3_c2.button("5", use_container_width=True):
    append_to_expression(5)
    st.rerun()
if r3_c3.button("6", use_container_width=True):
    append_to_expression(6)
    st.rerun()
if r3_c4.button("-", use_container_width=True):
    append_to_expression("-")
    st.rerun()

# --- Row 4 ---
if r4_c1.button("1", use_container_width=True):
    append_to_expression(1)
    st.rerun()
if r4_c2.button("2", use_container_width=True):
    append_to_expression(2)
    st.rerun()
if r4_c3.button("3", use_container_width=True):
    append_to_expression(3)
    st.rerun()
if r4_c4.button("+", use_container_width=True):
    append_to_expression("+")
    st.rerun()

# --- Row 5 ---
if r5_c1.button("0", use_container_width=True):
    append_to_expression(0)
    st.rerun()
if r5_c2.button(".", use_container_width=True):
    append_to_expression(".")
    st.rerun()
if r5_c3.button("=", use_container_width=True):
    evaluate_expression()
    st.rerun()

st.write("---")

# 5. Secret Code Tracker
secret_triggered = (st.session_state.expression == "Games123")

# 6. Smiley Face Corner Button & Secret Custom HTML Embed Trigger
col1, col2 = st.columns([6, 1])
with col2:
    if st.button("😊"):
        if secret_triggered:
            st.session_state["show_secret"] = True
        else:
            st.info("Just a friendly smiley face!")

# If the code matches 'Games123' and the smiley face is pressed, show the interface
if st.session_state["show_secret"]:
    st.success("Secret unlocked!")
    custom_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ANG€LIC V2</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Outfit:wght@300;500&display=swap" rel="stylesheet">
<style>
  :root {
    --gold: #ffd700;
    --amber: #ffb000;
    --ink: #07050a;
    --glow: .7;
    --speed: 1;xwez
    --orb: 280px;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; min-height: 100vh; font-family: Outfit, sans-serif; color: #fff4d0;
    text-transform: uppercase;
    background: radial-gradient(1200px 700px at 50% -10%, color-mix(in srgb, var(--gold) 28%, #000), var(--ink) 55%);
  }
  body::before, body::after { content: ""; position: fixed; inset: 0; pointer-events: none; }
  body::before {
    z-index: 0;
    background-image:
      radial-gradient(circle, #fff 1px, transparent 1.2px),
      radial-gradient(circle, var(--gold) 1px, transparent 1.5px),
      radial-gradient(circle, #ffe9a0 1.4px, transparent 1.8px);
    background-size: 90px 110px, 160px 130px, 240px 190px;
    animation: drift calc(40s / var(--speed)) linear infinite;
  }
  body.no-stars::before { display: none; }
  body::after {
    z-index: 0;
    background: linear-gradient(180deg, transparent, color-mix(in srgb, var(--gold) 18%, transparent) 50%, transparent);
    animation: sheen calc(6s / var(--speed)) ease-in-out infinite;
  }
  @keyframes drift { to { background-position: 80px 140px, -60px 90px, 40px -70px; } }
  @keyframes sheen { 50% { opacity: .55; } }
  #orb, #orb2 {
    position: fixed; left: 50%; top: 50%; z-index: 0; pointer-events: none; border-radius: 50%;
    transform: translate(-50%, -50%);
  }
  #orb {
    width: var(--orb); height: var(--orb);
    background: radial-gradient(circle, color-mix(in srgb, var(--gold) 85%, #fff) 0%, color-mix(in srgb, var(--gold) 35%, transparent) 42%, transparent 70%);
    box-shadow: 0 0 calc(80px * var(--glow)) calc(24px * var(--glow)) color-mix(in srgb, var(--gold) 45%, transparent), inset 0 0 50px rgba(255,245,180,.7);
    animation: glow calc(3.2s / var(--speed)) ease-in-out infinite;
  }
  #orb::before, #orb::after, #orb2 {
    content: ""; position: absolute; border-radius: 50%;
    border: 2px solid transparent; border-top-color: var(--gold); border-right-color: color-mix(in srgb, var(--gold) 35%, transparent);
    box-shadow: 0 0 calc(18px * var(--glow)) color-mix(in srgb, var(--gold) 70%, transparent);
    animation: spin calc(7s / var(--speed)) linear infinite;
  }
  #orb::before { inset: -22px; }
  #orb::after { inset: -48px; border-top-color: transparent; border-bottom-color: var(--gold); animation-duration: calc(12s / var(--speed)); animation-direction: reverse; }
  #orb2 { width: calc(var(--orb) * .55); height: calc(var(--orb) * .55); inset: auto; left: 18%; top: 22%; opacity: calc(.35 + var(--glow) * .4); animation-duration: calc(16s / var(--speed)); }
  @keyframes glow {
    0%, 100% { transform: translate(-50%, -50%) scale(.92); opacity: .65; }
    50% { transform: translate(-50%, -50%) scale(1.12); opacity: 1; }
  }
  @keyframes spin { to { transform: rotate(360deg); } }
  nav, main, #note { position: relative; z-index: 1; }
  #note {
    text-align: center; letter-spacing: .12em; font-size: 12px; padding: 12px; color: var(--gold);
    border-bottom: 1px solid color-mix(in srgb, var(--gold) 45%, transparent);
    background: linear-gradient(90deg, transparent, color-mix(in srgb, var(--gold) 22%, transparent), transparent);
    text-shadow: 0 0 12px var(--gold);
  }
  nav { display: flex; gap: 8px; padding: 14px; justify-content: center; flex-wrap: wrap; }
  nav button, button.act, .swatch {
    border: 1px solid color-mix(in srgb, var(--gold) 55%, transparent);
    background: rgba(20,12,0,.7); color: var(--gold); cursor: pointer;
    box-shadow: 0 0 calc(12px * var(--glow)) color-mix(in srgb, var(--gold) 25%, transparent);
  }
  nav button {
    min-width: 120px; padding: 12px 18px; border-radius: 999px;
    letter-spacing: .14em; font-family: Cinzel, serif; transition: .25s;
  }
  nav button:hover, button.act:hover { transform: translateY(-2px); box-shadow: 0 0 calc(22px * var(--glow)) var(--gold); }
  nav button.active { background: linear-gradient(180deg, color-mix(in srgb, var(--gold) 70%, #fff), var(--gold)); color: #1a1200; }
  main { padding: 8px 16px 40px; max-width: 760px; margin: auto; }
  .panel { display: none; animation: rise .35s ease; }
  .panel.active { display: block; }
  @keyframes rise { from { opacity: 0; transform: translateY(8px); } }
  #home { min-height: 62vh; display: none; place-items: center; }
  #home.active { display: grid; }
  #home h1 {
    margin: 0; font-family: Cinzel, serif; font-size: clamp(48px, 10vw, 96px);
    letter-spacing: .2em; color: color-mix(in srgb, var(--gold) 55%, #fff);
    text-shadow: 0 0 8px #fff, 0 0 calc(24px * var(--glow)) var(--gold), 0 0 calc(48px * var(--glow)) var(--amber), 0 0 calc(90px * var(--glow)) var(--gold);
    animation: bright calc(2.2s / var(--speed)) ease-in-out infinite;
  }
  @keyframes bright { 50% { filter: brightness(1.35); } }
  input, textarea, select {
    width: 100%; padding: 12px 14px; margin: 8px 0; border-radius: 14px;
    background: rgba(8,6,2,.75); color: #fff4d0; border: 1px solid color-mix(in srgb, var(--gold) 45%, transparent);
    outline: none; font: inherit; text-transform: uppercase;
    box-shadow: inset 0 0 calc(16px * var(--glow)) color-mix(in srgb, var(--gold) 12%, transparent);
  }
  input[type="file"], input[type="color"], input[type="range"], input[type="checkbox"] { text-transform: none; }
  input:focus, textarea:focus, select:focus { box-shadow: 0 0 0 3px color-mix(in srgb, var(--gold) 28%, transparent); }
  textarea { min-height: 130px; font-family: ui-monospace, monospace; }
  label { display: block; font-size: 12px; letter-spacing: .12em; color: var(--gold); margin-top: 10px; }
  button.act {
    padding: 9px 14px; border-radius: 999px; color: #1a1200; border: 0;
    background: linear-gradient(180deg, color-mix(in srgb, var(--gold) 65%, #fff), var(--gold));
    font-weight: 500; letter-spacing: .04em;
  }
  .row { display: flex; gap: 8px; flex-wrap: wrap; align-items: center; }
  .swatch { width: 34px; height: 34px; border-radius: 50%; padding: 0; }
  .swatch.on { outline: 2px solid #fff; }
  .game {
    display: flex; align-items: center; gap: 12px;
    margin: 12px 0; padding: 14px; border-radius: 18px;
    background: linear-gradient(180deg, rgba(40,28,0,.85), rgba(10,8,2,.9));
    border: 1px solid color-mix(in srgb, var(--gold) 45%, transparent);
    box-shadow: 0 10px 30px rgba(0,0,0,.35), 0 0 calc(18px * var(--glow)) color-mix(in srgb, var(--gold) 20%, transparent);
  }
  .cover {
    width: 72px; height: 72px; flex: 0 0 72px; border-radius: 14px; object-fit: cover;
    border: 1px solid color-mix(in srgb, var(--gold) 55%, transparent);
    box-shadow: 0 0 calc(12px * var(--glow)) color-mix(in srgb, var(--gold) 30%, transparent);
    background: #000;
  }
  .cover.ph {
    display: grid; place-items: center; font-family: Cinzel, serif; color: var(--gold);
    background: radial-gradient(circle, color-mix(in srgb, var(--gold) 35%, #000), #000 70%);
  }
  .meta { flex: 1; min-width: 0; }
  .meta span { display: block; overflow: hidden; text-overflow: ellipsis; }
  .actions { display: flex; gap: 8px; flex-wrap: wrap; justify-content: flex-end; }
  #preview {
    width: 120px; height: 120px; object-fit: cover; border-radius: 16px; display: none; margin: 8px 0;
    border: 1px solid color-mix(in srgb, var(--gold) 55%, transparent);
  }
  #modal { position: fixed; inset: 0; background: rgba(0,0,0,.82); display: grid; place-items: center; z-index: 4; backdrop-filter: blur(6px); }
  #modal[hidden] { display: none; }
  #box {
    width: min(900px, 92vw); height: min(640px, 86vh); display: flex; flex-direction: column;
    border-radius: 18px; overflow: hidden; background: #000;
    border: 1px solid var(--gold); box-shadow: 0 0 calc(40px * var(--glow)) var(--gold);
  }
  #box.full { width: 100vw; height: 100vh; border-radius: 0; border: 0; }
  #bar { display: flex; justify-content: space-between; align-items: center; padding: 10px 12px; background: #140e00; gap: 10px; }
  #gameTitle { font-family: Cinzel, serif; color: var(--gold); letter-spacing: .08em; text-shadow: 0 0 12px var(--gold); }
  #player { flex: 1; width: 100%; border: 0; background: #fff; }
</style>
</head>
<body>
<div id="orb"></div>
<div id="orb2"></div>
<div id="note">FOR THE GAMES TO WORK YOU MUST BE IN FULLSCREEN</div>
<nav>
  <button class="active" data-tab="home">HOME</button>
  <button data-tab="games">GAMES</button>
  <button data-tab="search">SEARCH</button>
  <button data-tab="library">LIBRARY</button>
  <button data-tab="look">LOOK</button>
</nav>
<main>
  <section id="home" class="panel active"><h1 id="hero">ANG€LIC</h1></section>
  <section id="games" class="panel">
    <form id="addForm">
      <input id="title" placeholder="GAME NAME" required>
      <label>COVER PICTURE</label>
      <input id="cover" type="file" accept="image/*">
      <input id="coverUrl" placeholder="OR PASTE IMAGE URL">
      <img id="preview" alt="">
      <textarea id="code" placeholder="PASTE HTML GAME CODE HERE"></textarea>
      <button class="act" type="submit">ADD</button>
    </form>
    <div id="list"></div>
  </section>
  <section id="search" class="panel">
    <input id="q" placeholder="SEARCH GAMES">
    <div id="results"></div>
  </section>
  <section id="library" class="panel">
    <p>SAVED GAMES.</p>
    <div id="saved"></div>
  </section>
  <section id="look" class="panel">
    <label>HOME TITLE</label>
    <input id="heroName" maxlength="18" value="ANG€LIC">
    <label>ACCENT</label>
    <div class="row" id="swatches">
      <button class="swatch" type="button" data-color="#ffd700" style="background:#ffd700"></button>
      <button class="swatch" type="button" data-color="#00e5ff" style="background:#00e5ff"></button>
      <button class="swatch" type="button" data-color="#ff2bd6" style="background:#ff2bd6"></button>
      <button class="swatch" type="button" data-color="#39ff14" style="background:#39ff14"></button>
      <button class="swatch" type="button" data-color="#ff4d4d" style="background:#ff4d4d"></button>
      <input id="customColor" type="color" value="#ffd700">
    </div>
    <label>GLOW <span id="glowVal">70</span></label>
    <input id="glow" type="range" min="10" max="160" value="70">
    <label>ORB SIZE <span id="orbVal">280</span></label>
    <input id="orbSize" type="range" min="120" max="520" value="280">
    <label>SPEED <span id="speedVal">1</span></label>
    <input id="speed" type="range" min="40" max="200" value="100">
    <label><input id="stars" type="checkbox" checked style="width:auto"> STAR FIELD</label>
    <button class="act" id="resetLook" type="button">RESET LOOK</button>
  </section>
</main>
<div id="modal" hidden>
  <div id="box">
    <div id="bar">
      <span id="gameTitle"></span>
      <span>
        <button class="act" id="fs" type="button">FULLSCREEN</button>
        <button class="act" id="close" type="button">X</button>
      </span>
    </div>
    <iframe id="player" sandbox="allow-scripts"></iframe>
  </div>
</div>
<script>
const KEY = "games";
const LOOK = "angelic-look";
const load = () => JSON.parse(localStorage.getItem(KEY) || "[]");
const save = (g) => localStorage.setItem(KEY, JSON.stringify(g));
const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const modal = document.getElementById("modal");
const box = document.getElementById("box");
const player = document.getElementById("player");
const root = document.documentElement;
const defaults = { accent: "#ffd700", glow: 70, orb: 280, speed: 100, stars: true, title: "ANG€LIC" };
function fileToCover(file) {
  return new Promise((resolve) => {
    if (!file) return resolve("");
    const img = new Image();
    const url = URL.createObjectURL(file);
    img.onload = () => {
      const max = 360;
      const scale = Math.min(1, max / Math.max(img.width, img.height));
      const c = document.createElement("canvas");
      c.width = Math.max(1, Math.round(img.width * scale));
      c.height = Math.max(1, Math.round(img.height * scale));
      c.getContext("2d").drawImage(img, 0, 0, c.width, c.height);
      URL.revokeObjectURL(url);
      resolve(c.toDataURL("image/jpeg", 0.72));
    };
    img.onerror = () => { URL.revokeObjectURL(url); resolve(""); };
    img.src = url;
  });
}
function coverHtml(g) {
  if (g.cover) return `<img class="cover" src="${esc(g.cover)}" alt="">`;
  return `<span class="cover ph">${esc((g.title || "?").slice(0, 1))}</span>`;
}
function applyLook(s) {
  root.style.setProperty("--gold", s.accent);
  root.style.setProperty("--amber", s.accent);
  root.style.setProperty("--glow", (s.glow / 100).toFixed(2));
  root.style.setProperty("--orb", s.orb + "px");
  root.style.setProperty("--speed", (s.speed / 100).toFixed(2));
  document.body.classList.toggle("no-stars", !s.stars);
  document.getElementById("hero").textContent = s.title || defaults.title;
  document.getElementById("glowVal").textContent = s.glow;
  document.getElementById("orbVal").textContent = s.orb;
  document.getElementById("speedVal").textContent = (s.speed / 100).toFixed(1);
  document.querySelectorAll(".swatch").forEach((b) => b.classList.toggle("on", b.dataset.color === s.accent));
}
function readLook() {
  return {
    accent: document.getElementById("customColor").value,
    glow: +document.getElementById("glow").value,
    orb: +document.getElementById("orbSize").value,
    speed: +document.getElementById("speed").value,
    stars: document.getElementById("stars").checked,
    title: document.getElementById("heroName").value.trim() || defaults.title
  };
}
function storeLook() {
  const s = readLook();
  localStorage.setItem(LOOK, JSON.stringify(s));
  applyLook(s);
}
function row(g, i) {
  return `<div class="game">${coverHtml(g)}<div class="meta"><span>${esc(g.title)}${g.saved ? " ★" : ""}</span></div><span class="actions">
    <button class="act" data-play="${i}">PLAY</button>
    <button class="act" data-cover="${i}">COVER</button>
    <button class="act" data-save="${i}">${g.saved ? "UNSAVE" : "SAVE"}</button>
    <button class="act" data-del="${i}">REMOVE</button></span></div>`;
}
function card(g) {
  return `<div class="game">${coverHtml(g)}<div class="meta"><span>${esc(g.title)}</span></div></div>`;
}
function render() {
  const games = load();
  document.getElementById("list").innerHTML = games.map(row).join("") || "<p>NO GAMES YET.</p>";
  document.getElementById("saved").innerHTML = games.filter((g) => g.saved).map(card).join("") || "<p>NOTHING SAVED.</p>";
  filter();
}
function filter() {
  const q = (document.getElementById("q").value || "").toLowerCase();
  document.getElementById("results").innerHTML = load().filter((g) => g.title.toLowerCase().includes(q)).map(card).join("") || "<p>NO MATCHES.</p>";
}
function closeGame() {
  if (document.fullscreenElement) document.exitFullscreen();
  box.classList.remove("full");
  player.srcdoc = "";
  modal.hidden = true;
}
function pickCover(done) {
  const input = document.createElement("input");
  input.type = "file";
  input.accept = "image/*";
  input.onchange = async () => done(await fileToCover(input.files[0]));
  input.click();
}
document.querySelectorAll("nav button").forEach((b) => b.onclick = () => {
  document.querySelectorAll("nav button, .panel").forEach((el) => el.classList.remove("active"));
  b.classList.add("active");
  document.getElementById(b.dataset.tab).classList.add("active");
});
document.getElementById("cover").onchange = async () => {
  const preview = document.getElementById("preview");
  const src = await fileToCover(document.getElementById("cover").files[0]);
  preview.src = src;
  preview.style.display = src ? "block" : "none";
};
document.getElementById("addForm").onsubmit = async (e) => {
  e.preventDefault();
  const title = document.getElementById("title"), code = document.getElementById("code");
  const file = document.getElementById("cover").files[0];
  const url = document.getElementById("coverUrl").value.trim();
  const games = load();
  games.push({ title: title.value.trim(), code: code.value, saved: false, cover: file ? await fileToCover(file) : url });
  save(games);
  e.target.reset();
  document.getElementById("preview").style.display = "none";
  render();
};
document.getElementById("list").onclick = (e) => {
  const games = load();
  const t = e.target;
  if (t.dataset.play != null) {
    const g = games[+t.dataset.play];
    document.getElementById("gameTitle").textContent = g.title;
    player.srcdoc = g.code || "<p>NO CODE SAVED.</p>";
    box.classList.remove("full");
    modal.hidden = false;
    return;
  }
  if (t.dataset.cover != null) {
    pickCover((src) => {
      if (!src) return;
      games[+t.dataset.cover].cover = src;
      save(games);
      render();
    });
    return;
  }
  if (t.dataset.del != null) games.splice(+t.dataset.del, 1);
  if (t.dataset.save != null) games[+t.dataset.save].saved = !games[+t.dataset.save].saved;
  save(games); render();
};
document.getElementById("close").onclick = closeGame;
document.getElementById("fs").onclick = () => {
  box.classList.toggle("full");
  if (box.classList.contains("full") && modal.requestFullscreen) modal.requestFullscreen();
  else if (document.fullscreenElement) document.exitFullscreen();
};
document.getElementById("q").oninput = filter;
["glow", "orbSize", "speed", "stars", "heroName", "customColor"].forEach((id) => {
  document.getElementById(id).oninput = storeLook;
});
document.getElementById("swatches").onclick = (e) => {
  const color = e.target.dataset.color;
  if (!color) return;
  document.getElementById("customColor").value = color;
  storeLook();
};
document.getElementById("resetLook").onclick = () => {
  localStorage.removeItem(LOOK);
  fillLook(defaults);
  applyLook(defaults);
};
function fillLook(s) {
  document.getElementById("customColor").value = s.accent;
  document.getElementById("glow").value = s.glow;
  document.getElementById("orbSize").value = s.orb;
  document.getElementById("speed").value = s.speed;
  document.getElementById("stars").checked = s.stars;
  document.getElementById("heroName").value = s.title;
}
const savedLook = JSON.parse(localStorage.getItem(LOOK) || "null") || defaults;
fillLook(savedLook);
applyLook(savedLook);
render();
</script>
</body>
</html>
    """
    components.html(custom_html, height=200)
