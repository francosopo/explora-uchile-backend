from django.db import models
from group.models import Grupo
from users.models import Anfitrion

# Create your models here.

class Partida(models.Model):
    id = models.IntegerField(primary_key=True)
    grupo = models.OneToOneField(Grupo,on_delete=models.CASCADE)
    anfitrion = models.ForeignKey(Anfitrion,on_delete=models.CASCADE)
    estado = models.CharField(max_length=255)

    def __str__(self):
        return self.id