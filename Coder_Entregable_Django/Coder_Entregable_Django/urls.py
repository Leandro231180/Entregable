"""Coder_Entregable_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app.models import Familiar
from app.views import familiar
from Coder_Entregable_Django.views import saludo, probando_template, template_por_loader

urlpatterns = [
    path('admin/', admin.site.urls),
    path('familia/', familiar), # Este Agrega a la Base de Datos y lo saca por pantalla
    path('saludame/', saludo),
    path('plant/', probando_template),
    path('fam/', template_por_loader),

]
