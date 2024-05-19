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

class AsignaTrabajoForm(forms.ModelForm):
  class Meta:
    model = Registro
    fields = ['especialista']

class EvaluaTrabajoForm(forms.ModelForm):
  class Meta:
    model = Registro
    fields = ['problema_real','tipo_de_problema']
    
class FinalizarTrabajoForm(forms.ModelForm):
  class Meta:
    model = Registro
    fields = ['solucionado','observaciones','fecha_salida']
    widgets = {
            'fecha_salida': DateInput(),
            }
    
class VerificarTrabajoForm(forms.ModelForm):
  class Meta:
    model = Registro
    fields = ['verificacion','fecha_verificacion']
    widgets = {
            'fecha_verificacion': DateInput(),
            }
  
class CreatePrioridadForm(forms.ModelForm):
  class Meta:
      model = Prioridad
      fields = '__all__'
      
class CreateEquipoForm(forms.ModelForm):
  class Meta:
      model = Equipo
      fields = '__all__'
