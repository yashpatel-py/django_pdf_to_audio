from django.urls import path
from . import views

urlpatterns = [
    path('', views.text_to_speech, name="audioToSpeech"),
]
