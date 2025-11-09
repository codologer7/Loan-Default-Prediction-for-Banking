# 🏦 Loan Risk Portal

**AI-powered loan default prediction platform with modern visuals, dynamic UI, and professional-grade backend.**  
Built using FastAPI, LightGBM, and Streamlit, this project helps financial institutions and individuals assess loan risk with precision and style.

---

## 🚀 Features

- 🔮 **Predict Loan Default Risk** using trained ML models
- 📊 **Probability & Risk Bucketing** for decision support
- 🎨 **Modern UI** with dark theme, glowing buttons, and gradient visuals
- ⚙️ **FastAPI Backend** for scalable model serving
- 🌐 **Streamlit Frontend** with multipage navigation
- 📈 **Feature Importance & Transparency** (optional)
- 🧠 **Model trained on Home Credit Default Risk dataset**

---

## 🧠 How It Works

1. **User inputs applicant data** via the frontend
2. **Streamlit sends request** to FastAPI backend (`/score`)
3. **Backend loads model** and returns:
   - Default probability
   - Risk bucket (A–D)
4. **Frontend displays results** with styled metrics and visuals

---

## 📁 Project Structure

```
Loan Risk Portal/
├─ Backend/
│  ├─ main.py                  # FastAPI app
│  └─ artifacts/               # Trained model (model_lgb.pkl)
├─ Home.py                     # Streamlit homepage
├─ pages/
│  └─ Loan Predictor.py        # Predictor UI
├─ .streamlit/
│  └─ config.toml              # Theme settings
├─ requirements.txt            # Python dependencies
├─ venv/                       # Virtual environment
```

---

## 🛠 Installation & Setup

### 1. Clone the repo
```bash
git clone https://github.com/your-username/loan-risk-portal.git
cd loan-risk-portal
```

### 2. Create virtual environment
```bash
python -m venv venv
```

### 3. Activate venv
```powershell
.\venv\Scripts\Activate.ps1      # Windows PowerShell
source venv/bin/activate         # macOS/Linux
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🧪 Run the App

### ▶️ Start Backend
```bash
cd Backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 🌐 Start Frontend
```bash
streamlit run Home.py
```

Visit: [http://localhost:8501](http://localhost:8501)

---

## 📦 API Endpoint

### `POST /score`
- **Request Body**:
```json
{
  "data": {
    "AMT_INCOME_TOTAL": 500000,
    "AMT_CREDIT": 200000,
    "AMT_ANNUITY": 12000,
    "DAYS_BIRTH": -12775,
    "DAYS_EMPLOYED": -2555,
    "CODE_GENDER": "F",
    "NAME_CONTRACT_TYPE": "Cash loans",
    "NAME_EDUCATION_TYPE": "Secondary / secondary special"
  }
}
```

- **Response**:
```json
{
  "pd": 0.142,
  "bucket": "B"
}
```

---

## 🎨 Design Highlights

- 🌌 Dark theme with purple gradients
- ✨ Glowing buttons on hover
- 📱 Responsive layout with two-column predictor
- 🖋️ Stylish fonts via Google Fonts (Poppins)
- 📈 Custom progress bars and metrics

---

## 📊 Model Details

- **Algorithm**: LightGBM
- **Calibrated with**: Isotonic Regression
- **Trained on**: [Home Credit Default Risk Dataset](https://www.kaggle.com/datasets/rakeshnereduapalli/home-credit-default-risk)
- **Features used**: Income, Credit, Annuity, Age, Employment, Gender, Contract Type, Education

---

## ✅ Requirements

```
fastapi
uvicorn
pandas
joblib
lightgbm
scikit-learn
streamlit
requests
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 📌 Credits

- Developed by Team 9 [Arpit Singh, Anjali Kumari, Abhay Singh, Shrijesh Kumar Choubey]
- Powered by FastAPI, Streamlit, LightGBM
- UI inspired by modern fintech dashboards

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.
