from pydoc import doc
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from datetime import date
from app.views import familiar
from django.template import loader



def saludo(request):
    return HttpResponse('Hola django')

# def probando_template(self):

#     miHtml= open('C:/DJANGO/Coder_Entregable_Django/Coder_Entregable_Django/Plantillas/templates.html')
#     plantilla= Template(miHtml.read())
#     miHtml.close()
#     mi_contexto=Context()
#     documento=plantilla.render(mi_contexto)

#     return HttpResponse(documento)

def probando_template(self):
    nom='Nico'
    ap='Perez'
    diccionario={'nombre':nom, 'apellido': ap}


    miHtml= open('C:/DJANGO/Coder_Entregable_Django/Coder_Entregable_Django/Plantillas/templates.html')
    plantilla= Template(miHtml.read())
    miHtml.close()
    mi_contexto=Context(diccionario)
    documento=plantilla.render(mi_contexto)

    return HttpResponse(documento)


def template_por_loader(self):

    nom='LEO'
    ap='thunder'
    diccionario={'nombre':nom, 'apellido': ap}

    plantilla= loader.get_template('plantillaFamilia.html')

    docu = plantilla.render(diccionario)

    return HttpResponse(docu)

