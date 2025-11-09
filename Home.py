import streamlit as st

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
<style>
html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>
/* Gradient background */
body {
    background: linear-gradient(135deg, #2c003e, #0e0e0e);
}

/* Glowing purple button */
div.stButton > button {
    background-color: #a704e7ff;
    color: white;
    border-radius: 8px;
    border: none;
    font-size: 1.1em;
    font-weight: bold;
    transition: 0.3s;
}
div.stButton > button:hover {
    box-shadow: 0 0 40px #a704e7ff;
    background-color: #a704e7ff;
    transform: scale(1.05);
}

/* Headings with gradient text */
h1, h2, h3 {
    background: linear-gradient(90deg, #a704e7ff, #e056fd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-family: 'Poppins', sans-serif;
}
</style>
""", unsafe_allow_html=True)


st.set_page_config(page_title="Loan Risk Portal", page_icon="💳", layout="wide")

# Hero section
st.markdown("""
<div style="text-align:center; padding:80px; background:linear-gradient(135deg,#6a0dad,#000000); border-radius:15px;">
    <h1 style="color:white; font-size:3em; font-family:'Poppins',sans-serif;">🏦 Loan Risk Portal</h1>
    <p style="color:#ddd; font-size:1.2em;">AI-powered loan default prediction with stunning visuals</p>
</div>
""", unsafe_allow_html=True)

st.write("")
if st.button("🔮 Open Loan Default Risk Predictor", use_container_width=True):
    st.switch_page("pages/LoanPredictor.py")

st.divider()
st.header("📖 About")
st.write("Our platform helps financial institutions and individuals evaluate loan risk using advanced machine learning models.")

st.header("⚙️ How It Works")
col1, col2, col3 = st.columns(3)
col1.info("Step 1: Enter Applicant Data")
col2.success("Step 2: AI Predicts Risk")
col3.warning("Step 3: Get Probability + Bucket")

st.divider()
st.caption("© 2025 Loan Risk Portal • Built by Team 9")
