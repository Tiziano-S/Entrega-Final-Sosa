from django.shortcuts import render, redirect
from .models import Publicacion
from django.conf import settings
from .forms import PostForm
print(settings.DATABASES)

def lista_publicacion(request):
    busqueda= request.GET.get("busqueda", None)
    if busqueda:
        lista_publicaciones = Publicacion.objects.filter(titulo__icontains=busqueda)
    else:
        lista_publicaciones = Publicacion.objects.all()
    return render(request, "blog/lista_publicaciones.html", context= {"publicacion": lista_publicaciones})

def crear_publicacion(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.author = request.user
                post.save()
                return redirect('blog:lista_publicacion')
            else:
                form.add_error(None,"User must be logged in to create a post.")
    else:
        form = PostForm()
    return render(request,"blog/crear_publicacion.html", context={"form":form})