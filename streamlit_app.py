import streamlit as st

st.set_page_config(page_title="Virginia Calculator", page_icon="🧮", layout="centered")

# Initialize session state for expression tracking
if "expression" not in st.session_state:
    st.session_state.expression = ""

st.title("Virginia Calculator")
st.subheader("Standard Calculator")

# Display screen
st.text_input("Result", value=st.session_state.expression, key="display", label_visibility="collapsed", disabled=True)

# Grid Layout for Buttons
buttons = [
    ["C", "(", ")", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

# Render layout grid
for row in buttons:
    cols = st.columns(len(row))
    for idx, btn_text in enumerate(row):
        if cols[idx].button(btn_text, use_container_width=True):
            if btn_text == "C":
                st.session_state.expression = ""
            elif btn_text == "=":
                try:
                    # Format standard layout operator symbols to evaluatable Python
                    eval_expr = st.session_state.expression.replace("÷", "/").replace("×", "*")
                    if eval_expr:
                        st.session_state.expression = str(eval(eval_expr))
                except Exception:
                    st.session_state.expression = "Error"
            else:
                if st.session_state.expression == "Error":
                    st.session_state.expression = ""
                st.session_state.expression += btn_text
            st.rerun()

st.write("---")

# Spacer columns to position the smiley face on the bottom right
col1, col2, col3 = st.columns([6, 1, 1])

with col3:
    # -------------------------------------------------------------
    # 📝 REPLACE EVERYTHING BETWEEN THESE TRIPLE QUOTES WITH YOUR HTML:
    my_custom_page = """
:)
    """
    # -------------------------------------------------------------

    # This dynamically encodes your HTML code string into an address link
    smiley_html = f"""
    <a href="data:text/html;charset=utf-8,{my_custom_page}" target="_blank" style="text-decoration: none;">
        <button style="
            width: 100%;
            background-color: white;
            border: 1px solid #d3d3d3;
            padding: 8px 16px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 18px;
            box-shadow: 0px 1px 3px rgba(0,0,0,0.1);
            transition: 0.2s;">
            😊
        </button>
    </a>
    """
    st.components.v1.html(smiley_html, height=50)
