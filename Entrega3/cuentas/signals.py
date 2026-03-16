from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import PerfilAutor, EstadisticasAutor

@receiver(post_save, sender=User)
def create_author_models(sender, instance, created, **kwargs):

    if created:
        PerfilAutor.objects.create(usuario=instance)
        EstadisticasAutor.objects.create(usuario=instance)