from django import forms
from Models.proyecto1.models import proyecto1

class Formularioproyecto1(forms.ModelForm):
 class Meta:
     model= proyecto1    
     fields='_all_'
     widgets={'fecha_nacimiento':forms.DateInput(attrs={'type':'date'})}
     
