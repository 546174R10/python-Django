from django.http import HttpResponse
from django.template.loader import get_template

class HomeView():
#    home
    def home(self):
      plantilla = get_template('index.html')
      return HttpResponse(plantilla.render())    
#  pagina1
    def pagina1(self):
     return HttpResponse('Hola desde una nueva ruta')
    # pagina2
    def pagina2(self, parametro1) :
     return HttpResponse('Hola desde una nueva ruta con parametro' + str(parametro1))
    # pagina3
    def pagina3(self, parametro1, parametro2):
     return HttpResponse('Hola desde una nueva ruta con parametro' + str(parametro1) + '-'+ str(parametro2))
 
    def formulario(self):
     plantilla = get_template('formulario.html')
     return HttpResponse(plantilla.render())