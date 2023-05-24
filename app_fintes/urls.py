"""
URL configuration for app_fintes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the i nclude() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fitnes.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eye/', training_eye),
    path('hand/', training_hand),
    path('neck/', training_neck),
    path('leg/', training_leg),
    path('back/', training_back)

]
