from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# -----------------------------------------------
# Estas son las clases para la gestión del taller
# -----------------------------------------------

class TipoProblema(models.Model):
    nombre = models.CharField(max_length=50)
    class Meta:
        db_table_comment = "Clasificación de tipos de problema"

    def __str__(self):
        return self.nombre

class TipoEquipo(models.Model):
    nombre = models.CharField(max_length=50)
    class Meta:
        db_table_comment = "Clasificación de tipos de equipo"

    def __str__(self):
        return self.nombre
    
class Prioridad(models.Model):
    nombre = models.CharField(max_length=50)
    class Meta:
        db_table_comment = "Clasificación de Prioridad"

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    tipo = models.ForeignKey(TipoEquipo, on_delete=models.CASCADE)
    inventario = models.CharField(max_length=20)
    class Meta:
        db_table_comment = "Detalles del equipo"

    def __str__(self):
        return self.inventario

class Especialista(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    class Meta:
        db_table_comment = "Especialista"

    def __str__(self):
        return self.nombre
    
class Entidad(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    class Meta:
        db_table_comment = "detalles de la Entidad"

    def __str__(self):
        return self.nombre


class Registro(models.Model):
    ESTADOS = [
        ("RECEPCIONADO", "Recepcionado"),
        ("ASIGNADO", "Asignado"),
        ("EVALUADO", "Evaluado"),
        ("EN_PROCESO", "En proceso"),
        ("FINALIZADO", "Finalizado"),
    ]
    
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    nombre_responsable = models.CharField(max_length=100)
    telefono_responsable = models.CharField(max_length=12)
    fecha_entrada = models.DateField()
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    problema_reportado = models.TextField()
    prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS,default="RECEPCIONADO")
    
    especialista = models.ForeignKey(Especialista, on_delete=models.SET_NULL, null=True)
    problema_real = models.TextField(blank=True, null=True)
    tipo_de_problema = models.ForeignKey(TipoProblema, on_delete=models.SET_NULL, null=True)
    
    solucionado = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True, null=True)
    fecha_salida = models.DateField(blank=True, null=True)
    
    verificado = models.BooleanField(default=False)
    verificacion = models.TextField(blank=True, null=True)
    fecha_verificacion = models.DateField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Registro de {self.equipo.nombre} {self.equipo.modelo} - Responsable: {self.nombre_responsable}"
