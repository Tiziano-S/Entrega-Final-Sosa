from django.shortcuts import render
from .models import Publicacion

def lista_publicacion(request):
    lista_publicaciones = Publicacion.objects.all()
    return render(request, "blog/lista_publicaciones.html", context= {"publicacion": lista_publicaciones})