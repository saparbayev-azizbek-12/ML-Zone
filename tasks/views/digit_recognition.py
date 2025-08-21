import os
import io
import json
import joblib
import base64
import numpy as np
from PIL import Image
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from tasks.services.digit_recognition import predict

model_path = os.path.join(settings.BASE_DIR, 'models', 'digit_recognition', 'digit_clf.joblib')
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
            image_data = data.get('image_data')

            format, imgstr = image_data.split(';base64,')
            image_bytes = base64.b64decode(imgstr)
            
            image = Image.open(io.BytesIO(image_bytes)).convert('L').resize((28, 28))

            # np -> normalize -> flatten list
            image_np = np.array(image, dtype=float) / 255.0
            image_flat = image_np.reshape(-1).tolist()
            res = predict(image_flat)
            if res['status']:
                digit = int(res['data'])
                return JsonResponse({'prediction': digit})
            else:
                return JsonResponse({'error': res['message']})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'digit_recognition/index.html')
