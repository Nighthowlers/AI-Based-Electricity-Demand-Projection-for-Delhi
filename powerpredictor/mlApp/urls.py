from django.urls import path
from . import views

urlpatterns = [
    path('', views.Predictor, name = 'Predictor'),
    path('submit/', views.formInfo, name = 'formInfo'),
]