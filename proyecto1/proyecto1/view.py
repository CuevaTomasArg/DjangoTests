from django.http import HttpResponse
from django.template import Template, Context
import datetime
from django.template import loader

def salud(request):
    return HttpResponse("Que asee gatooooo")

def dia_de_hoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"Hoy es dia: {dia}"
    return HttpResponse(documentoDeTexto)

def probandoTemplate(self):
    nom = "Tomas"
    ap = "Cueva"
    
    listaDeNotas = [2,2,2,22,2,2,2,2,2,2,2,2]
    
    diccionario = {
        "nombre":nom,
        "apellido":ap,
        "notas":listaDeNotas,
    }
    
    # miHtml = open("C:\\Users\\tomas\\OneDrive\\Escritorio\\python\\pruebaEntornoVirtual\\proyecto1\\proyecto1\\plantillas\\template1.html")
    #plantilla = Template(miHtml.read())
    
    #miHtml.close()
    #miContexto = Context(diccionario)
    #documento = plantilla.render(miContexto)
    plantilla = loader.get_template('template2.html')
    
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
    
    