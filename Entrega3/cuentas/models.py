from django.db import models
from django.contrib.auth.models import User

class PerfilAutor(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.TextField()
    region = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.usuario.username

class EstadisticasAutor(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    publicaciones_hechas = models.IntegerField(default=0)

    def __str__(self):
        return f"Stats for {self.usuario.username}"
