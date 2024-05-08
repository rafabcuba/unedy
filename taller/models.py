from django.db import models
from django.utils import timezone

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
    
class Equipo(models.Model):
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    inventario = models.CharField(max_length=255)
    
    def __str__(self):
        return self.inventario

class Registro(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha = models.DateField()
    problema_reportado = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    problema_real = models.CharField(max_length=255, null=True, blank=True)   
    tipo_de_problema = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.problema_reportado