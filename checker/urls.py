# users/urls.py
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('check/', views.check, name='check'), 
    path('text/', views.output_text, name='outputtext'), 
]