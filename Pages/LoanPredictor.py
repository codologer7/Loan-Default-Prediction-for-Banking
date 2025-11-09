import streamlit as st
import requests


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
    font-weight: extra-bold;
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


st.set_page_config(page_title="Loan Default Risk Predictor", page_icon="📈", layout="wide")

st.title("Loan Default Risk Predictor")
st.caption("Enter applicant details to assess risk.")

API_URL = "http://localhost:8000/score"

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Applicant Information")
    income = st.number_input("Annual Income (₹)", min_value=0.0, value=500000.0, step=1000.0)
    credit = st.number_input("Loan Amount Requested (₹)", min_value=0.0, value=200000.0, step=1000.0)
    annuity = st.number_input("Monthly Installment (₹)", min_value=0.0, value=12000.0, step=500.0)
    age = st.number_input("Age (Years)", min_value=18, max_value=80, value=35)
    employment = st.number_input("Employment Duration (Years)", min_value=0, max_value=50, value=7)
    gender = st.radio("Gender", ["Male", "Female"])
    contract = st.selectbox("Loan Type", ["Cash loans", "Revolving loans"])
    education = st.selectbox("Education Level", [
        "Secondary / secondary special",
        "Higher education",
        "Incomplete higher",
        "Lower secondary",
        "Academic degree"
    ])
    submitted = st.button("Predict Risk", use_container_width=True)

with col2:
    st.subheader("Prediction Results")
    if submitted:
        payload = {
            "data": {
                "AMT_INCOME_TOTAL": income,
                "AMT_CREDIT": credit,
                "AMT_ANNUITY": annuity,
                "DAYS_BIRTH": -(age * 365),
                "DAYS_EMPLOYED": -(employment * 365),
                "CODE_GENDER": "M" if gender == "Male" else "F",
                "NAME_CONTRACT_TYPE": contract,
                "NAME_EDUCATION_TYPE": education
            }
        }

        r = requests.post(API_URL, json=payload)
        if r.status_code == 200:
            res = r.json()
            pd = res["pd"]
            bucket = res["bucket"]

            st.metric("Default Probability", f"{pd:.2%}")
            st.metric("Risk Bucket", bucket)

            
            # Purple progress bar
            progress_html = f"""
            <div style="background-color:#333; border-radius:10px; height:20px;">
                <div style="width:{pd*100}%; background:linear-gradient(90deg,#9b59b6,#e056fd); height:20px; border-radius:10px;"></div>
            </div>
            """
            st.markdown(progress_html, unsafe_allow_html=True)


            if pd < 0.1:
                st.success("✅ Very Low Risk (Bucket A)")
            elif pd < 0.2:
                st.info("ℹ️ Moderate Risk (Bucket B)")
            elif pd < 0.3:
                st.warning("⚠️ High Risk (Bucket C)")
            else:
                st.error("❌ Very High Risk (Bucket D)")
        else:
            st.error("API error: " + r.text)
