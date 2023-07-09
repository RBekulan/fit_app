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
# from fitnes.views import *
from category.views import *
from pro_fersion.views import *
from users.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/eye/', EyeTrainingView.as_view()),
    path('api/v1/hand/', HandTrainingView.as_view()),
    path('api/v1/neck/', NeckTrainingView.as_view()),
    path('api/v1/leg/', LegTrainingView.as_view()),
    path('api/v1/back/', BackTrainingView.as_view()),
    path('api/v1/plusversion/', ProVersionView.as_view()),
    path('api/v1/register/', RegisterView.as_view()),
    path('api/v1/authorizations/', AuthorizationView.as_view()),
    path('api/v1/start/', StartStopView.as_view())

]
