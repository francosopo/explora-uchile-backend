from django.db import models

# Create your models here.
class Grupo(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    min_integrantes = models.IntegerField()
    max_integrantes = models.IntegerField()

    def __str__(self):
        return self.nombre

    def set_group_name(self, nombre):
        self.nombre = nombre

    def ready(self):
        # return self.min_integrantes <= 
        pass