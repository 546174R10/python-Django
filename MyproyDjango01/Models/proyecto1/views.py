from django.http import HttpRequest
from django.shortcuts import render
from Models.proyecto1.forms import Formularioproyecto1


class Formularioproyecto1View(HttpRequest):
     
     def index(request):
         proyecto1= Formularioproyecto1()
         return render(request,"AlumnoIndex.html",{"form":proyecto1})
     
     def procesar_formulario(request):
         proyecto1 =Formularioproyecto1()
         if proyecto1.is_valid():
             proyecto1.save()
             proyecto1=Formularioproyecto1()
             return render(request,"AlumnoIndex.html",{"form":proyecto1, "mensaje":'OK'}) 