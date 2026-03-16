from django.urls import path
from . import views

app_name = "cuentas"

urlpatterns = [
    path("", views.perfil, name="pagina_autor"),
    path("crear/", views.crear_perfil, name="crear_perfil"),
    path("registro/", views.registro, name="registro"),
]