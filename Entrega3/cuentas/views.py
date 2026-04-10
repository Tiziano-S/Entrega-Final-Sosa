from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import PerfilAutor
from .forms import AuthorProfileForm
from blog.models import Publicacion
from .forms import RegistroUsuarioForm, EditUserForm, AvatarForm
from django.contrib.auth import login
from .models import Avatar

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
        avatar_form = AvatarForm()

    return render(request, "cuentas/registro.html", {
        "form": form,
        "avatar_form": avatar_form
    })

def editar_perfil(request):
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=request.user)
        
        try:
            avatar = request.user.avatar
        except Avatar.DoesNotExist:
            avatar = None

        if avatar:
            avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        else:
            avatar_form = AvatarForm(request.POST, request.FILES)

        if form.is_valid() and avatar_form.is_valid():
            form.save()
            avatar_instance = avatar_form.save(commit=False)
            avatar_instance.user = request.user
            avatar_instance.save()
            return redirect("cuentas:pagina_autor")

    else:    
        form = EditUserForm(instance = request.user)
        if hasattr(request.user, "avatar"):
            avatar_form = AvatarForm(instance = request.user.avatar)
        else:
            avatar_form = AvatarForm()
    return render(request, "cuentas/editar_perfil.html", {"form": form, "avatar_form": avatar_form})