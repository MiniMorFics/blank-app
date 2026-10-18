import streamlit as st
import streamlit.components.v1 as components
import urllib.parse

# 1. Main Application Header
st.title("VA Calculator")
st.subheader("Standard Calculator")

# 2. Initialize Session States
if "expression" not in st.session_state:
    st.session_state.expression = ""

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

# 3. Native Screen Input Line
st.session_state.expression = st.text_input(
    "Calculator Screen Display",
    value=st.session_state.expression,
    label_visibility="collapsed",
    placeholder="0"
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

# 5. Secret Code Tracker Rules
current_word = st.session_state.expression.strip()
secret_triggered = current_word in ["Games123", "Gamer123", "Gamers123"]

# 6. Smiley Face Corner Button Trigger
col1, col2 = st.columns([6, 1])
with col2:
    if secret_triggered:
        # Define the complete HTML portal document payload (with backslash fix)
        portal_html = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ANG€LIC V2</title>
<link href="https://googleapis.com" rel="stylesheet">
<style>
:root {
--gold: #ffd700;
--amber: #ffb000;
--ink: #07050a;
--glow: .7;
--speed: 1;
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
animation: drift 40s linear infinite;
}
body.no-stars::before { display: none; }
body::after {
z-index: 0;
background: linear-gradient(180deg, transparent, color-mix(in srgb, var(--gold) 18%, transparent) 50%, transparent);
animation: sheen 6s ease-in-out infinite;
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
animation: glow 3.2s ease-in-out infinite;
}
#orb::before, #orb::after, #orb2 {
content: ""; position: absolute; border-radius: 50%;
border: 2px solid transparent; border-top-color: var(--gold); border-right-color: color-mix(in srgb, var(--gold) 35%, transparent);
box-shadow: 0 0 calc(18px * var(--glow)) color-mix(in srgb, var(--gold) 70%, transparent);
animation: spin 7s linear infinite;
}
#orb::before { inset: -22px; }
#orb::after { inset: -48px; border-top-color: transparent; border-bottom-color: var(--gold); animation-duration: 12s; animation-direction: reverse; }
#orb2 { width: calc(var(--orb) * .55); height: calc(var(--orb) * .55); inset: auto; left: 18%; top: 22%; opacity: calc(.35 + var(--glow) * .4); animation-duration: 16s; }
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
animation: bright 2.2s ease-in-out infinite;
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
