import os
import json
import joblib
import numpy as np
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse


model_path = os.path.join(settings.BASE_DIR, 'tasks', 'models', 'house_price_model.pkl')
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
                float(data['area']),
                int(data['bedrooms']),
                int(data['bathrooms']),
                int(data['stories'])
            ]
            
            input_data = np.array(features).reshape(1, -1)
            
            prediction = model.predict(input_data)
            price = float(prediction[0])
            
            return JsonResponse({'prediction': price})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'house_price/index.html')
