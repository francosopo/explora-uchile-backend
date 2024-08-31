from django.db import models


# Create your models here.

class Place(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)

    class Meta:
        abstract = True
        
    def __str__(self):
        return self.nombre

class Campus(Place):
    pass
    
class Facultad(Place):
    campus = models.ForeignKey(Campus,on_delete=models.CASCADE)

class Lugar(Place):
    #id = models.IntegerField(primary_key=True)
    coordenadas = models.CharField(max_length=255)
    facultad = models.ForeignKey(Facultad,on_delete=models.CASCADE)