from django.db import models

# Create your models here.

class Estudiante (models.Model):
    cedula=models.CharField(primary_key=True, max_length=10 )
    nombre=models.CharField (max_length=30, black =False) 
    apellido=models.TextField ()
    edad=models.IntegerField()
    direccion=models.TextField ()
    telefono=models.CharField(max_length=10, black =False)

def __str__(self):
    return self.nombre
class Docente (models.Model):
    cedula=models.CharField(primary_key=True, max_length=10 )
    nombre=models.CharField (max_length=30, black =False) 
    apellido=models.TextField ()
    edad=models.IntegerField()
    direccion=models.TextField ()
    telefono=models.CharField(max_length=10, black =False)

def __str__(self):
    return self.nombre

class Calificacion (models.Model):
    cedula_estu= models.ForeignKey(Calificacion,  on_delete=models.RESTRICT)
    cedula_doc=models.ForeignKey(Calificacion,  on_delete=models.RESTRICT)
    calificacion=models.FloatField()
    


