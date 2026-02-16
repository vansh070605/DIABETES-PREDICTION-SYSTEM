from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from .ml.predictor import predict_diabetes

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def welcome():
    """Landing page with hero section and CTA"""
    return render_template('welcome.html')

@main_bp.route('/about')
def about():
    """About page with AI information"""
    return render_template('about.html')

@main_bp.route('/features')
def features():
    """Features page showcasing benefits"""
    return render_template('features.html')

@main_bp.route('/contact')
def contact():
    """Contact page with information"""
    return render_template('contact.html')

@main_bp.route('/predict')
def predict():
    """Prediction form page"""
    return render_template('predict.html')

@main_bp.route('/result', methods=['POST'])
def result():
    """Result display page"""
    try:
        input_data = {
            'pregnancies': int(request.form.get('pregnancies', 0)),
            'glucose': float(request.form.get('glucose', 0)),
            'blood_pressure': int(request.form.get('blood_pressure', 0)),
            'skin_thickness': int(request.form.get('skin_thickness', 0)),
            'insulin': int(request.form.get('insulin', 0)),
            'bmi': float(request.form.get('bmi', 0)),
            'diabetes_pedigree': float(request.form.get('diabetes_pedigree', 0)),
            'age': int(request.form.get('age', 0))
        }
        
        # Use ML model for prediction
        prediction_result = predict_diabetes(input_data)
        
        result_data = {
            'risk_level': prediction_result['risk_level'],
            'risk_class': prediction_result['risk_class'],
            'category': prediction_result['category'],
            'confidence': int(prediction_result['confidence']),
            'date': datetime.now().strftime('%B %d, %Y')
        }
        
        return render_template('result.html', result=result_data)
        
    except (ValueError, TypeError, Exception) as e:
        print(f"Error in prediction: {e}")
        # Use endpoint name including blueprint prefix
        return redirect(url_for('main.predict'))
