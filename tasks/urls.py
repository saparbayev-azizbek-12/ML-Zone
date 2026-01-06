from django.urls import path
from .views import house_price, digit_recognition, spam_classifier, iris_classifier, fashion_classifier, smart_join

app_name = 'tasks'

urlpatterns = [
    path('house-price/', house_price.index, name='house_price'),
    path('digit-recognition/', digit_recognition.index, name='digit_recognition'),
    path('spam-classifier/', spam_classifier.index, name='spam_classifier'),
    path('iris-classifier/', iris_classifier.index, name='iris_classifier'),
    path('fashion-classifier/', fashion_classifier.index, name='fashion_classifier'),
    path('smart-join/', smart_join.index, name='smart_join'),
    path('smart-join/upload/', smart_join.upload, name='smart_join_upload'),
    path('smart-join/run-join/', smart_join.run_join, name='smart_join_run_join'),
]
