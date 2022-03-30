from tabnanny import verbose
from django.db import models
import datetime
# Create your models here.


class Empleo(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    category = models.TextField(blank=False, null=False)
    requisitos = models.TextField(blank=False, null=False)
    oferta = models.TextField(blank=False, null=False)
   
def _str_(self): 
    return self.titulo

class Empleo_profesional(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    category = models.TextField(blank=False, null=False)
    requisitos = models.TextField(blank=False, null=False)
    oferta = models.TextField(blank=False, null=False)
   
def _str_(self): 
    return self.categoria

class Empleo_bajo_nivel(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    category = models.TextField(blank=False, null=False)
    requisitos = models.TextField(blank=False, null=False)
    oferta = models.TextField(blank=False, null=False)
   
def _str_(self): 
    return self.oferta

class Comentarios(models.Model):
    nombre = models.CharField(max_length=150, blank=False, null=False)
    telefono = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=150, blank=False, null=False)
    comentario = models.TextField(blank=False, null=False)

class Meta:
    verbose_name = ("Comment")
    verbose_name_plural = ("Comment")

def _str_(self): 
    return self.comentario
