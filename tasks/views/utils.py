import os
import uuid 
import joblib
import numpy as np
from PIL import Image
from datetime import datetime
from django.conf import settings

def preprocess_image(file_obj):
    image = Image.open(file_obj).convert("L")
    image = image.resize((28, 28))
    img_array = np.array(image)
    img_array = 255 - img_array
    img_array = img_array.reshape(1, -1)
    return img_array

def file_name_generator(file_obj):
    file_extension = file_obj.name.split('.')[-1]  # Get last part after dot
    datetime_now = datetime.now().strftime('%Y%m%d%H%M%S%f')
    uuid_current = str(uuid.uuid4())[:8]  # Convert to string and get first 8 chars
    return f"{datetime_now}_{uuid_current}.{file_extension}"

def get_model(folder, model_name):
    model_path = os.path.join(settings.BASE_DIR, 'models', folder, f'{model_name}.joblib')
    try:
        model = joblib.load(model_path)
    except FileNotFoundError:
        model = None
    return model

def save_file(file_obj, file_name, subdirectory='fashion'):
    # Create subdirectory if it doesn't exist
    subdirectory_path = os.path.join(settings.MEDIA_ROOT, subdirectory)
    os.makedirs(subdirectory_path, exist_ok=True)
    
    # Save file in subdirectory
    file_path = os.path.join(subdirectory_path, file_name)
    with open(file_path, 'wb') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)