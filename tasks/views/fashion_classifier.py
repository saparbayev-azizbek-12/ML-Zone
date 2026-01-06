from django.conf import settings
from django.shortcuts import render
from .constants import class_names
from .utils import preprocess_image, file_name_generator, get_model, save_file

def index(request):
    context = {}
    try:
        model = get_model('fashion_classifier', 'fashion_mnist')
        scaler = get_model('fashion_classifier', 'scaler')
    except Exception as e:
        model = None
        scaler = None
    
    if request.method == 'POST':
        if model is None:
            context['error'] = 'Model not found.'
        else:
            try:
                img_file = request.FILES.get('img')
                if not img_file:
                    context['error'] = 'No image file provided.'
                else:
                    file_name = file_name_generator(img_file)
                    save_file(img_file, file_name, 'fashion')
                    img_file.seek(0)
                    X = preprocess_image(img_file)
                    X = scaler.transform(X)
                    pred = model.predict(X)[0]

                    context['prediction'] = class_names[pred]
                    context['filename'] = file_name
                    context['uploaded_image'] = f"{settings.MEDIA_URL}fashion/{file_name}"
                    print(context['uploaded_image'])
            except Exception as e:
                context['error'] = str(e)

    return render(request, 'fashion_classifier/index.html', context)
