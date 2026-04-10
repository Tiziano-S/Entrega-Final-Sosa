from django.shortcuts import render, redirect
from .models import Publicacion
from django.conf import settings
from .forms import PostForm
from django.views.generic import ListView, DetailView
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
                post.autor = request.user
                post.save()
                return redirect('blog:lista_publicacion')
            else:
                form.add_error(None,"User must be logged in to create a post.")
    else:
        form = PostForm()
    return render(request,"blog/crear_publicacion.html", context={"form":form})

def form_valid(self, form):
    form.instance.autor = self.request.user
    return super().form_valid(form)

class VistaListaPublicaciones(ListView):
    model = Publicacion
    template_name = "blog/lista_publicaciones.html"
    context_object_name = "publicaciones"

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda", None)
        if busqueda:
            queryset = queryset.filter(titulo__icontains=busqueda)
        return queryset
    
class VistaPublicacionDetalle(DetailView):
    model = Publicacion
    template_name = "blog/publicacion_detalle.html"