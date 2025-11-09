# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib, json

app = FastAPI(title="Loan Default Predictor")

# Load artifacts at startup
model = joblib.load("artifacts/model_lgb.pkl")
calibrator = joblib.load("artifacts/calibrator_iso.pkl")
encoders = joblib.load("artifacts/label_encoders.pkl")
medians = joblib.load("artifacts/feature_medians.pkl")
meta = json.load(open("artifacts/artifacts_meta.json"))
feature_columns = meta["feature_columns"]
cutoffs = meta["cutoffs"]

class Applicant(BaseModel):
    data: dict  # {"AMT_INCOME_TOTAL": 120000, "CODE_GENDER": "M", ...}

def safe_transform_with_encoders(df, encoders):
    df = df.copy()
    for col, le in encoders.items():
        if col not in df.columns:
            df[col] = ""
        df[col] = df[col].astype(str)
        known = set(le.classes_)
        fallback = next(iter(known))
        df[col] = df[col].apply(lambda x: x if x in known else fallback)
        df[col] = le.transform(df[col])
    return df

def assign_bucket(p, cuts):
    if p <= cuts["A"]: return "A"
    if p <= cuts["B"]: return "B"
    if p <= cuts["C"]: return "C"
    return "D"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/score")
def score(applicant: Applicant):
    df = pd.DataFrame([applicant.data])
    # Align to training columns
    for c in feature_columns:
        if c not in df.columns:
            df[c] = pd.NA
    df = df[feature_columns]
    # Encode + fill missing
    df = safe_transform_with_encoders(df, encoders)
    num_cols = medians.index.tolist()
    df[num_cols] = df[num_cols].fillna(medians)
    # Predict raw and calibrate
    raw = model.predict_proba(df)[:, 1]
    pd_cal = calibrator.transform(raw)
    bucket = assign_bucket(pd_cal[0], cutoffs)
    return {"pd": float(pd_cal[0]), "bucket": bucket}
