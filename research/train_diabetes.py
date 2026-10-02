import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

print(f"USING SCIKIT-LEARN VERSION: {sklearn.__version__}")

# 1. Load data
csv_path = 'diabetes.csv'
if not os.path.exists(csv_path):
    print(f"Error: {csv_path} not found! Ensure the csv is in the same folder as this script.")
else:
    df = pd.read_csv(csv_path)

    # 2. Features and Target
    # Ensure columns match your dataset: Pregnancies, Glucose, BloodPressure, etc.
    X = df.drop('Outcome', axis=1) 
    y = df['Outcome']

    # 3. Model Training
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # 4. Save the brain for handover
    joblib.dump(model, 'diabetes_model.pkl')
    print("MISSION ACCOMPLISHED: diabetes_model.pkl generated for LG-YAM team.")