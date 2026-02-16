"""
Predictor - ML model prediction logic with input validation
"""
import numpy as np
from .model_loader import ModelLoader

def predict_diabetes(data):
    """
    Predict diabetes risk using trained ML model
    
    Args:
        data (dict): Dictionary containing:
            - pregnancies (int): Number of pregnancies
            - glucose (float): Glucose level (mg/dL)
            - blood_pressure (int): Blood pressure (mm Hg)
            - skin_thickness (int): Skin thickness (mm)
            - insulin (int): Insulin level (μU/mL)
            - bmi (float): Body Mass Index (kg/m²)
            - diabetes_pedigree (float): Diabetes Pedigree Function
            - age (int): Age (years)
    
    Returns:
        dict: Prediction results containing:
            - prediction (int): 0 or 1
            - probability (float): Probability of diabetes (0-100)
            - risk_level (str): Low/Medium/High Risk
            - risk_class (str): CSS class name
            - category (str): Risk category description
            - confidence (int): Confidence percentage
    """
    # Load the model
    model = ModelLoader.get_model()
    
    # Prepare input features in the correct order
    # Order must match training data: Pregnancies, Glucose, BloodPressure, 
    # SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age
    features = np.array([[
        data['pregnancies'],
        data['glucose'],
        data['blood_pressure'],
        data['skin_thickness'],
        data['insulin'],
        data['bmi'],
        data['diabetes_pedigree'],
        data['age']
    ]])
    
    # Get prediction (0 or 1)
    prediction = model.predict(features)[0]
    
    # Get probability scores for both classes
    probability = model.predict_proba(features)[0]
    
    # Probability of diabetes (class 1)
    diabetes_prob = probability[1] * 100
    
    # Determine risk level based on probability
    if diabetes_prob < 30:
        risk_level = "Low Risk"
        risk_class = "low-risk"
        category = "Minimal Concern"
    elif diabetes_prob < 60:
        risk_level = "Medium Risk"
        risk_class = "medium-risk"
        category = "Moderate Concern"
    else:
        risk_level = "High Risk"
        risk_class = "high-risk"
        category = "Significant Concern"
    
    # Confidence is the maximum probability
    confidence = max(probability) * 100
    
    return {
        'prediction': int(prediction),
        'probability': round(diabetes_prob, 2),
        'risk_level': risk_level,
        'risk_class': risk_class,
        'category': category,
        'confidence': round(confidence, 0)
    }
