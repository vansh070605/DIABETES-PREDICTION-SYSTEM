"""
Model Loader - Singleton pattern to load and cache the trained model
"""
import joblib
import os
from pathlib import Path

class ModelLoader:
    """Singleton class to load and cache the diabetes prediction model"""
    _model = None
    
    @classmethod
    def get_model(cls):
        """
        Load the trained model (cached after first load)
        
        Returns:
            Trained LogisticRegression model
        """
        if cls._model is None:
            # Get the path to the model file
            current_dir = Path(__file__).resolve().parent
            model_path = current_dir / 'diabetes_model.pkl'
            
            if not model_path.exists():
                raise FileNotFoundError(
                    f"Model file not found at {model_path}. "
                    "Please run train_model.py first."
                )
            
            # Load the model
            cls._model = joblib.load(model_path)
            print(f"Model loaded from: {model_path}")
        
        return cls._model
