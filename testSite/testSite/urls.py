"""testSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from testSite.views import saludo, dameFecha,calculaEdad
from testAPI.views import *
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('hora/', dameFecha),
    path('param/<int:edad>/<int:agno>', calculaEdad),
    path('API/', PropList.as_view()),
    path('API2/<int:pk>', PropDetail.as_view()),
    path('API2/', PropDetail.as_view()),
    path('token22/', views.obtain_auth_token),
    path('token/', Auth.as_view() ),      


]