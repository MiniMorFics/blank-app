import urllib.parse
import streamlit as st

# --- 1. SET UP THE VIRGINIA CALCULATOR DISPLAY ---
st.title("Virginia Calculator")
st.subheader("Standard Calculator")

# Initialize calculator state variables if they don't exist yet
if "calc_input" not in st.session_state:
    st.session_state.calc_input = ""

# Display screen for the calculator output (Using a clean header to show text dynamically)
if st.session_state.calc_input:
    st.code(st.session_state.calc_input, language="text")
else:
    st.code("0", language="text")

# --- 2. CALCULATOR GRID LAYOUT ---
# Row 1: Clear and basic operators
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("C", use_container_width=True):
        st.session_state.calc_input = ""
        st.rerun()
with col2:
    if st.button("(", use_container_width=True):
        st.session_state.calc_input += "("
        st.rerun()
with col3:
    if st.button(")", use_container_width=True):
        st.session_state.calc_input += ")"
        st.rerun()
with col4:
    if st.button("÷", use_container_width=True):
        st.session_state.calc_input += "/"
        st.rerun()

# Row 2: 7, 8, 9, x
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("7", use_container_width=True):
        st.session_state.calc_input += "7"
        st.rerun()
with col2:
    if st.button("8", use_container_width=True):
        st.session_state.calc_input += "8"
        st.rerun()
with col3:
    if st.button("9", use_container_width=True):
        st.session_state.calc_input += "9"
        st.rerun()
with col4:
    if st.button("×", use_container_width=True):
        st.session_state.calc_input += "*"
        st.rerun()

# Row 3: 4, 5, 6, -
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("4", use_container_width=True):
        st.session_state.calc_input += "4"
        st.rerun()
with col2:
    if st.button("5", use_container_width=True):
        st.session_state.calc_input += "5"
        st.rerun()
with col3:
    if st.button("6", use_container_width=True):
        st.session_state.calc_input += "6"
        st.rerun()
with col4:
    if st.button("-", use_container_width=True):
        st.session_state.calc_input += "-"
        st.rerun()

# Row 4: 1, 2, 3, +
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("1", use_container_width=True):
        st.session_state.calc_input += "1"
        st.rerun()
with col2:
    if st.button("2", use_container_width=True):
        st.session_state.calc_input += "2"
        st.rerun()
with col3:
    if st.button("3", use_container_width=True):
        st.session_state.calc_input += "3"
        st.rerun()
with col4:
    if st.button("+", use_container_width=True):
        st.session_state.calc_input += "+"
        st.rerun()

# Row 5: 0, ., =
col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    if st.button("0", use_container_width=True):
        st.session_state.calc_input += "0"
        st.rerun()
with col2:
    if st.button(".", use_container_width=True):
        st.session_state.calc_input += "."
        st.rerun()
with col3:
    if st.button("=", use_container_width=True):
        try:
            if st.session_state.calc_input:
                st.session_state.calc_input = str(eval(st.session_state.calc_input))
        except Exception:
            st.session_state.calc_input = "Error"
        st.rerun()

st.write("---")

import base64  # Make sure this import is included at the top or here

# --- 3. CUSTOM HTML POPUP SECTION ---
st.write("---")

# 1. Your raw dashboard code
my_custom_html = """<!DOCTYPE html>
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
            animation: drift calc(40s / var(--speed)) linear infinite;
        }
        @keyframes drift { to { background-position: 80px 140px, -60px 90px, 40px -70px; } }
        #orb {
            position: fixed; left: 50%; top: 50%; z-index: 0; pointer-events: none; border-radius: 50%;
            transform: translate(-50%, -50%); width: var(--orb); height: var(--orb);
            background: radial-gradient(circle, color-mix(in srgb, var(--gold) 85%, #fff) 0%, color-mix(in srgb, var(--gold) 35%, transparent) 42%, transparent 70%);
        }
        nav, main, #note { position: relative; z-index: 1; }
        #note {
            text-align: center; letter-spacing: .12em; font-size: 14px; padding: 20px; color: var(--gold);
            text-shadow: 0 0 12px var(--gold);
        }
        h1 { text-align: center; font-family: Cinzel, serif; font-size: 64px; color: var(--gold); margin-top: 20vh; }
    </style>
</head>
<body>
    <div id="orb"></div>
    <div id="note">FOR THE GAMES TO WORK YOU MUST BE IN FULLSCREEN</div>
    <main>
        <h1>ANG€LIC V2</h1>
    </main>
</body>
</html>"""

# 2. Encode the HTML to base64 so quotes/backticks don't break the JS script below
b64_html = base64.b64encode(my_custom_html.encode('utf-8')).decode('utf-8')

# 3. Build the custom button that utilizes window.open('about:blank')
smiley_link_button = f"""
<button id="dashBtn" style="
    width: 100%;
    background-color: #2b2b2b;
    color: white;
    border: 1px solid #444;
    padding: 14px 16px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 22px;
    font-family: sans-serif;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    transition: 0.2s;">
    😊 Open Custom Dashboard
</button>

<script>
document.getElementById('dashBtn').addEventListener('click', function() {{
    // 1. Grab the encoded HTML payload
    var b64Data = "{b64_html}";
    
    // 2. Decode the base64 data safely handling UTF-8 special characters
    var decodedHtml = new TextDecoder().decode(Uint8Array.from(atob(b64Data), c => c.charCodeAt(0)));
    
    # 3. Open a completely blank top-level tab
    var newWindow = window.open('about:blank', '_blank');
    
    if (newWindow) {{
        // 4. Inject your custom code into the blank workspace document stream
        newWindow.document.open();
        newWindow.document.write(decodedHtml);
        newWindow.document.close();
    }} else {{
        alert('Popup blocked! Please allow popups in your browser settings to open the dashboard.');
    }}
}});
</script>
"""

# Render the button launcher block
st.components.v1.html(smiley_link_button, height=90)


# Safely encode the page content to bypass special character collision
safe_url_layout = urllib.parse.quote(my_custom_html)

smiley_link_button = f"""
<a href="data:text/html;charset=utf-8,{safe_url_layout}" target="_blank" style="text-decoration: none;">
    <button style="
        width: 100%;
        background-color: #2b2b2b;
        color: white;
        border: 1px solid #444;
        padding: 14px 16px;
        border-radius: 8px;
        cursor: pointer;
        font-size: 22px;
        font-family: sans-serif;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
        transition: 0.2s;">
        😊 Open Custom Dashboard
    </button>
</a>
"""

# Render the button container cleanly inside Streamlit
st.components.v1.html(smiley_link_button, height=90)
