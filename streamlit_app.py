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

# 5. String Match Rule Verification
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

# 7. Main Environment Transition Sequence
if st.session_state["show_secret"]:
    st.success("Redirecting environment...")
    
    # Active execution layer designed to push the context frame outwards
    breakout_script = """
    <script>
    (function() {
        var payload = `
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>ANG€LIC V2</title>
            <style>
                :root {
                    --gold: #ffd700;
                    --ink: #07050a;
                }
                * { box-sizing: border-box; }
                body {
                    margin: 0; min-height: 100vh; font-family: sans-serif; color: #fff4d0;
                    text-transform: uppercase;
                    background: radial-gradient(1200px 700px at 50% -10%, #3a3000, var(--ink) 55%);
                    display: flex; flex-direction: column; align-items: center; justify-content: center;
                }
                #note {
                    position: absolute; top: 0; width: 100%; text-align: center; 
                    letter-spacing: .12em; font-size: 12px; padding: 12px; color: var(--gold);
                    border-bottom: 1px solid rgba(255,215,0,0.4);
                    background: linear-gradient(90deg, transparent, rgba(255,215,0,0.1), transparent);
                }
                h2 { color: var(--gold); letter-spacing: 0.15em; font-weight: bold; }
                p { font-size: 14px; color: #ffe9a0; }
            </style>
        </head>
        <body>
            <div id="note">FOR THE GAMES TO WORK YOU MUST BE IN FULLSCREEN</div>
            <h2>ANG€LIC CONSOLE SANDBOX</h2>
            <p>WELCOME TO YOUR CUSTOM EMBEDDED SANDBOX ENVIRONMENT.</p>
            <p style="color: gray; font-size: 12px;">STATUS: READY.</p>
        </body>
        </html>
        `;
        
        // Break out of the Streamlit iframe sandbox context explicitly
        var targetWindow = window.parent || window;
        
        // Open a completely clean window instance
        var newWin = targetWindow.open();
        if (newWin) {
            newWin.document.open();
            newWin.document.write(payload);
            newWin.document.close();
        } else {
            alert("Popup blocked! Please allow popups for this app to open the external sandbox environment.");
        }
    })();
    </script>
    """
    # Execute the layout shift code block immediately
    components.html(breakout_script, height=0, width=0)
    
    # Reset internal switch to ensure subsequent attempts run cleanly
    st.session_state["show_secret"] = False
