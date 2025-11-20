"""
URL configuration for powerpredictor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from powerpredictor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('login_button', views.Predictor, name='Predictor'),
    path('Predictor.html/', views.Predictor, name='Predictor'),
    path('Predictor', views.home, name='Home'),
    path('imp-Links/', views.ImpLinks, name="Important Links"),
    path('distribution/', views.Distribution, name="Distribution"),
    path('help-us/', views.helpUS, name="Help Desk"),
    path('about-us/', views.aboutUS, name="About"),
    # path('Predictor', views.formInfo,name='Predictor'),
    path('Predictor', include('mlApp.urls')),

    # path('admin/', admin.site.urls),
    # path('', views.login, name='login'),
    # path('predictor/', views.Predictor, name='Predictor'),
    # path('home/', views.home, name='Home'),
    # path('', include('mlApp.urls')),
]
