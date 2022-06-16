from django.shortcuts import render
from django.http import HttpResponse
from app.models import Familiar

# Create your views here.

def familiar(self):
    
    familiar= Familiar(nombre='Leandro', edad=41, fecha_nacimiento="1980-11-23")
    familiar.save()

    familiar2= Familiar(nombre='Sebastian', edad=38, fecha_nacimiento="1984-01-25")
    familiar2.save()

    familiar3= Familiar(nombre='Mauro', edad=35, fecha_nacimiento="1987-09-19")
    familiar3.save()

    documento= f'Mi familiar se llana {familiar.nombre}, tiene {familiar.edad}, y nacio el dia {familiar.fecha_nacimiento} , mi otro familiar se llama {familiar2.nombre} tiene {familiar2.edad} y nacio en {familiar2.fecha_nacimiento}. y por ultimo lo mi hermano mas chico se llama {familiar3.nombre}, tiene {familiar3.edad} y nacion en {familiar3.fecha_nacimiento}'

    return HttpResponse(documento)
