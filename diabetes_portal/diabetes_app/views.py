from django.shortcuts import render
import joblib
import os
import pandas as pd

# 1. Load the Diabetes Brain
def load_diabetes_model():
    path = os.path.join(os.path.dirname(__file__), 'diabetes_model.pkl')
    return joblib.load(path)

model = load_diabetes_model()

def index(request):
    return render(request, 'index.html')

def predict(request):
    if request.method == 'POST':
        try:
            # Getting data from the YAM team's form
            data = {
                'Pregnancies': int(request.POST.get('pregnancies', 0)),
                'Glucose': float(request.POST.get('glucose', 0)),
                'BloodPressure': float(request.POST.get('bp', 0)),
                'SkinThickness': float(request.POST.get('skin', 0)),
                'Insulin': float(request.POST.get('insulin', 0)),
                'BMI': float(request.POST.get('bmi', 0)),
                'DiabetesPedigreeFunction': float(request.POST.get('dpf', 0)),
                'Age': int(request.POST.get('age', 0))
            }

            features = pd.DataFrame([data])
            prediction = model.predict(features)

            result = "Positive (High Risk)" if prediction[0] == 1 else "Negative (Normal)"
            return render(request, 'result.html', {'result': result})
        except Exception as e:
            return render(request, 'index.html', {'error': str(e)})
    return render(request, 'index.html')