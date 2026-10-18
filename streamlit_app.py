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

# 3. Clean Native Entry Line (Replaces the broken display sandbox completely)
# Users can click here and type smoothly on a hardware keyboard without desyncs
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

# 5. Broad Code Tracker (Accepts all variants cleanly)
current_word = st.session_state.expression.strip()
secret_triggered = current_word in ["Games123", "Gamer123", "Gamers123"]

# 6. Smiley Face Corner Button Trigger
col1, col2 = st.columns([6, 1])
with col2:
    if st.button("😊"):
        if secret_triggered:
            st.session_state["show_secret"] = True
        else:
            st.info("Just a friendly smiley face!")

# If validated, mount the complete verified game layout frame from your repository
if st.session_state["show_secret"]:
    st.success("Secret unlocked!")
    
    custom_html = """
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
            body::before {
                content: ""; position: fixed; inset: 0; pointer-events: none; z-index: 0;
                background-image: 
                    radial-gradient(circle, #fff 1px, transparent 1.2px),
                    radial-gradient(circle, var(--gold) 1px, transparent 1.5px),
                    radial-gradient(circle, #ffe9a0 1.4px, transparent 1.8px);
                background-size: 90px 110px, 160px 130px, 240px 190px;
                animation: drift 40s linear infinite;
            }
            @keyframes drift { to { background-position: 80px 140px, -60px 90px, 40px -70px; } }
            #note {
                text-align: center; letter-spacing: .12em; font-size: 12px; padding: 12px; color: var(--gold);
                border-bottom: 1px solid color-mix(in srgb, var(--gold) 45%, transparent);
                background: linear-gradient(90deg, transparent, color-mix(in srgb, var(--gold) 22%, transparent), transparent);
                text-shadow: 0 0 12px var(--gold);
            }
            h3 { font-family: Cinzel, serif; color: var(--gold); text-align: center; margin-top: 20px; }
            p { text-align: center; font-family: Outfit, sans-serif; }
        </style>
    </head>
    <body>
        <div id="note">FOR THE GAMES TO WORK YOU MUST BE IN FULLSCREEN</div>
        <h3>ANG€LIC Console Sandbox</h3>
        <p>Welcome to your custom embedded sandbox environment.</p>
        <p style="color: gray; font-size: 12px;">Status: Ready.</p>
    </body>
    </html>
    """
    components.html(custom_html, height=300)
