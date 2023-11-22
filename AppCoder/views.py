from django.shortcuts import render
from django.http import HttpResponse

def view_inicio(xx):
    return HttpResponse("Bienvenidos !!!!!!!!")

def view_cursos(xx):
    return render(xx, "AppCoder/padre.html")
# Create your views here.
