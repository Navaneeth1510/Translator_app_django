# translate_app/urls.py
from django.urls import path
from translate_app.views import translate_text

urlpatterns = [
    path('translate/', translate_text, name='translate'),
]
