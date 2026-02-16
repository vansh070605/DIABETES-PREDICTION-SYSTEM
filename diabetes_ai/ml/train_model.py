"""
Train and save the diabetes prediction model
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

# Load the dataset
data = pd.read_csv('diabetes.csv')

# Separate features and target
X = data.drop(columns='Outcome', axis=1)
Y = data['Outcome']

# Split the data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Train the model
print("Training Logistic Regression model...")
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

# Evaluate the model
predictions = model.predict(X_test)
accuracy = accuracy_score(Y_test, predictions)
print(f"Model Accuracy: {accuracy:.4f}")

# Create ml_model directory if it doesn't exist
ml_model_dir = os.path.join('DiabetesPrediction', 'ml_model')
os.makedirs(ml_model_dir, exist_ok=True)

# Save the model
model_path = os.path.join(ml_model_dir, 'diabetes_model.pkl')
joblib.dump(model, model_path)
print(f"Model saved to: {model_path}")

# Test loading the model
loaded_model = joblib.load(model_path)
test_predictions = loaded_model.predict(X_test)
test_accuracy = accuracy_score(Y_test, test_predictions)
print(f"Loaded model accuracy: {test_accuracy:.4f}")
print("Model training and saving completed successfully!")
