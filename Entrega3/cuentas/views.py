from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import PerfilAutor
from .forms import AuthorProfileForm
from blog.models import Publicacion
from .forms import RegistroUsuarioForm
from django.contrib.auth import login

@login_required
def perfil(request):
    try:
        profile = request.user.perfilautor
    except PerfilAutor.DoesNotExist:
        return redirect("cuentas:crear_perfil")

    publicaciones = Publicacion.objects.filter(autor=request.user)

    return render(request, "cuentas/pagina_autor.html", {
        "profile": profile,
        "posts": publicaciones
    })

@login_required
def crear_perfil(request):

    if PerfilAutor.objects.filter(usuario=request.user).exists():
        return redirect("cuentas:pagina_autor")

    if request.method == "POST":
        form = AuthorProfileForm(request.POST)

        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.usuario = request.user
            perfil.save()

            return redirect("cuentas:pagina_autor")

    else:
        form = AuthorProfileForm()

    return render(request, "cuentas/crear_perfil.html", {
        "form": form
    })

def registro(request):

    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("cuentas:crear_perfil")

    else:
        form = RegistroUsuarioForm()

    return render(request, "cuentas/registro.html", {
        "form": form
    })