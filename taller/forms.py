from django import forms
from .models import Registro, Prioridad, Equipo

class DateInput(forms.DateInput):
    input_type = 'date'

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
    
    widgets = {
            'fecha_entrada': DateInput(),
            }
  
class CreatePrioridadForm(forms.ModelForm):
  class Meta:
      model = Prioridad
      fields = '__all__'
      
class CreateEquipoForm(forms.ModelForm):
  class Meta:
      model = Equipo
      fields = '__all__'
