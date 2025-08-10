import os
import json
import joblib
import numpy as np
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

# Correct path to the model file
model_path = os.path.join(settings.BASE_DIR, 'models', 'iris_classifier', 'iris_dataset_classifier.joblib')
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    model = None

def index(request):
    if request.method == 'POST':
        if model is None:
            return JsonResponse({'error': 'Model not found.'}, status=500)

        try:
            data = json.loads(request.body)
            features = [
                float(data['sepal_length']),
                float(data['sepal_width']),
                float(data['petal_length']),
                float(data['petal_width'])
            ]
            
            flower_names = {
                0: 'Iris-setosa',
                1: 'Iris-versicolor',
                2: 'Iris-virginica'
            }
            input_data = np.array([features])
            print(input_data)
            
            prediction = model.predict(input_data)
            print(prediction)
            species = flower_names[prediction[0]]
            
            return JsonResponse({'prediction': species})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'iris_classifier/index.html')
