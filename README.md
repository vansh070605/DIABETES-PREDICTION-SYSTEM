# 🩺 Diabetes Prediction System  

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)  ![Django](https://img.shields.io/badge/Django-Web%20Framework-green?logo=django)  ![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)  ![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-yellow?logo=scikitlearn)  ![SQLite](https://img.shields.io/badge/SQLite-Database-lightblue?logo=sqlite)  

## 📌 Project Overview  
This is a **Diabetes Prediction System** that combines:  
- ✅ **Machine Learning (Logistic Regression)** trained on the PIMA Diabetes dataset.  
- ✅ **Django Web Application** for user interaction and predictions.  
- ✅ **Jupyter Notebook** for ML experimentation.  

The system predicts whether a person is diabetic or not based on medical input data.  

---

## 📂 Project Structure  

```bash
DIABETES-PREDICTION-SYSTEM/
│── .venv/                     # Virtual environment
│── DiabetesPrediction/        # Django project
│   │── __pycache__/           
│   │── __init__.py
│   │── asgi.py
│   │── settings.py
│   │── urls.py
│   │── views.py
│   │── wsgi.py
│   │── static/DiabetesPrediction/images/
│   │   └── heart.jpg
│   │── templates/
│   │   └── home.html
│── db.sqlite3                 # SQLite database
│── manage.py                  # Django entry point
│── diabetes.csv               # Dataset
│── diabetes.ipynb             # ML Notebook (training & evaluation)
│── README.md                  # Documentation
````

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/vansh070605/DIABETES-PREDICTION-SYSTEM.git
cd DIABETES-PREDICTION-SYSTEM

# Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run Django server
python manage.py runserver
```

---

## 🚀 Usage

### 🧑‍💻 Run Jupyter Notebook (ML Model)

```bash
jupyter notebook diabetes.ipynb
```

### 🌐 Run Django Web App

```bash
python manage.py runserver
```

Then open 👉 `http://127.0.0.1:8000/` in your browser.

---

## 📊 Results

<details>
  <summary>Click to expand</summary>

* Logistic Regression trained on **PIMA Diabetes Dataset**.
* Achieved **\~75–80% accuracy**.
* Visualizations: heatmaps, null-value plots, correlation matrix.

Accuracy Output:

```text
Model Accuracy: 0.77
```

</details>

---

## 🔮 Future Enhancements

* Add other ML models (Random Forest, SVM, XGBoost).
* Integrate **Flask/Streamlit** for lightweight deployment.
* Deploy Django app on **Heroku / Vercel / AWS**.
* Add user authentication for personalized predictions.

---

## 👨‍💻 Author

**Vansh Agrawal**

📌 Connect with me:
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/thevanshagrawal)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/vansh070605)