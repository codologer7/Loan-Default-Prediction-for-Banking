import streamlit as st
import requests

st.set_page_config(page_title="Loan Risk Predictor", page_icon="💳", layout="wide")

st.title("💳 Loan Default Risk Predictor")
st.markdown("Enter applicant details below to assess risk.")

API_URL = "http://localhost:8000/score"

# Two-column layout: inputs on left, results on right
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📋 Applicant Information")
    income = st.number_input("Annual Income (₹)", min_value=0.0, value=500000.0, step=1000.0)
    credit = st.number_input("Loan Amount Requested (₹)", min_value=0.0, value=200000.0, step=1000.0)
    annuity = st.number_input("Monthly Installment (₹)", min_value=0.0, value=12000.0, step=500.0)
    age = st.number_input("Age (Years)", min_value=18, max_value=80, value=35)
    employment = st.number_input("Employment Duration (Years)", min_value=0, max_value=50, value=7)
    gender = st.radio("Gender", ["Male", "Female"])
    contract = st.selectbox("Loan Type", ["Cash Loan", "Revolving Loan"])
    education = st.selectbox("Education Level", [
        "Secondary / secondary special",
        "Higher education",
        "Incomplete higher",
        "Lower secondary",
        "Academic degree"
    ])
    submitted = st.button("🔮 Predict Risk")

with col2:
    st.header("📊 Prediction Results")
    if submitted:
        payload = {
            "data": {
                "AMT_INCOME_TOTAL": income,
                "AMT_CREDIT": credit,
                "AMT_ANNUITY": annuity,
                "DAYS_BIRTH": -(age*365),  # convert years to days
                "DAYS_EMPLOYED": -(employment*365),
                "CODE_GENDER": "M" if gender == "Male" else "F",
                "NAME_CONTRACT_TYPE": contract,
                "NAME_EDUCATION_TYPE": education
            }
        }

        r = requests.post(API_URL, json=payload)
        if r.status_code == 200:
            res = r.json()
            pd = res['pd']
            bucket = res['bucket']

            st.metric("Default Probability", f"{pd:.2%}")
            st.metric("Risk Bucket", bucket)

            if pd < 0.1:
                st.success("✅ Very Low Risk (Bucket A)")
            elif pd < 0.2:
                st.info("ℹ️ Moderate Risk (Bucket B)")
            elif pd < 0.3:
                st.warning("⚠️ High Risk (Bucket C)")
            else:
                st.error("❌ Very High Risk (Bucket D)")

            st.progress(min(pd, 1.0))
        else:
            st.error("API error: " + r.text)
