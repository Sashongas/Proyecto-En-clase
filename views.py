from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader

def saludo(request):
    return HttpResponse("Soy Nico - Hola Django - Coder")

def segundaVista(request):
    return HttpResponse("<br><br> SOMOS PROGRAMADORES AHRE")

def  dia(request):
    variable = datetime.now()
    return HttpResponse(f"Hoy es un gran dia {variable}")

def apellido(request, ape):
    fecha = datetime.now()
    return HttpResponse(f"El profe de coder {ape}, es muy bueno...<br>")

def probandoTemplate(request):
  mejorEstudiante = "El loco"
  nota = 9.8
  estudiantesMasSimpaticos = ["Juanse", "Nadia", "Cristo", "Laura"]

  dicc = {"nombre:": mejorEstudiante, "nota:": nota, "estudiantes:": estudiantesMasSimpaticos}

  plantilla=  loader.get_template("template1.html")

    #miHTML = open("C:/Users/sashi/Documents/Python/Proyecto1/Proyecto1/plantillas/template1.html")
    #plantilla = Template(miHTML.read())
    #miHTML.close()
    #miContexto = Context(dicc)
    #documento = plantilla.render(miContexto)
    
  documento = plantilla.render(dicc)
  return HttpResponse(documento) 