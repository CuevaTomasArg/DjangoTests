from http.client import HTTPResponse
from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
def curso(self):
    
    curso = Curso(nombre="Desarrollo web",camada="1234151")
    curso.save()
    documento_de_texto = f"-->Curso: {curso.nombre} Camada:{curso.camada}"
    
    return  HttpResponse(documento_de_texto)
# Create your views here.
