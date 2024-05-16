from django import forms
from .models import Registro, Prioridad

class CreateRegistroForm(forms.ModelForm):
  class Meta:
    model = Registro
    fields = ['equipo', 
              'nombre_responsable', 
              'telefono_responsable',
              'fecha_entrada',
              'entidad',
              'problema_reportado',
              'prioridad'
              ]
  
class CreatePrioridadForm(forms.ModelForm):
  class Meta:
      model = Prioridad
      fields = ['nombre']
