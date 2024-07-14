# translate_app/urls.py
from django.urls import path
from .views import translate_text

urlpatterns = [
    path('translate/', translate_text, name='translate'),
]