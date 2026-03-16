from django.urls import path
from . import views
app_name = "blog"
urlpatterns = [
    path("lista/publicaciones", views.lista_publicacion, name= "lista_publicacion"),
    path("crear/publicacion", views.crear_publicacion, name="crear_publicacion")
]