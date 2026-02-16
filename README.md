# 🩺 Diabetes Prediction System  

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)  ![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey?logo=flask)  ![Modern UI](https://img.shields.io/badge/Premium-UI/UX-blueviolet)  ![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-yellow?logo=scikitlearn)

## 📌 Project Overview  
This is a **Modern AI-Powered Diabetes Risk Assessment System** that combines clinical precision with a premium user experience.  

### ✨ Key Features
- 🚀 **Advanced ML Model**: Utilizes a Logistic Regression model trained on clinical data for reliable risk prediction.
- 🎨 **Premium "Lavender Dream" UI**: A state-of-the-art, glassmorphic design featuring smooth animations and a responsive layout.
- 🎬 **Dynamic Motion**: Integrated scroll-triggered animations (reveal effects) and interactive hover states.
- ⚡ **Real-Time Analysis**: Instant results processed through a lightweight Flask backend.
- 🔒 **Privacy-First**: Zero-retention policy; health metrics are processed in real-time and never stored.

---

## 📂 Project Structure  

```bash
DIABETES-PREDICTION-SYSTEM/
├── diabetes_ai/            # Main Application Package
│   ├── ml/                 # ML Logic & Model
│   │   ├── model_loader.py
│   │   ├── predictor.py
│   │   └── diabetes_model.pkl
│   ├── static/             # Assets (CSS, SVG)
│   ├── templates/          # HTML Templates
│   ├── __init__.py         # App Initialization
│   └── routes.py           # Application Routes
├── run.py                  # Entry Point
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/vansh070605/DIABETES-PREDICTION-SYSTEM.git
cd DIABETES-PREDICTION-SYSTEM

# Create & activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
```

---

## 🚀 Usage

1. **Launch the Server**: Run `python app.py`.
2. **Access the Portal**: Open `http://127.0.0.1:8000` in your browser.
3. **Start Assessment**: Navigate to the "Predict" page, enter clinical metrics (Glucose, BMI, etc.), and receive an instant AI risk analysis.

---

## � Model Performance

- **Algorithm**: Logistic Regression
- **Accuracy**: ~75-80%
- **Metrics Evaluated**: pregnancies, glucose, blood pressure, skin thickness, insulin, BMI, diabetes pedigree function, and age.

---

## 👨‍💻 Author

**Vansh Agrawal**

📌 Connect with me:
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/thevanshagrawal)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/vansh070605)