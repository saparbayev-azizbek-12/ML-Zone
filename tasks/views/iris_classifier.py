import json
from django.shortcuts import render
from django.http import JsonResponse
from tasks.services.iris_classifier import predict


def index(request):
    if request.method == 'POST':

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
            
            pred = predict(features)
            if pred['status']:
                species = flower_names[pred['data']]
                return JsonResponse({'prediction': species})
            else:
                return JsonResponse({'error': "Something went wrong with the prediction service!"})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'iris_classifier/index.html')
