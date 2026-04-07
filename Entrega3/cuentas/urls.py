from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "cuentas"

urlpatterns = [
    path("", views.perfil, name="pagina_autor"),
    path("crear/", views.crear_perfil, name="crear_perfil"),
    path("registro/", views.registro, name="registro"),
    path("editar_perfil", views.editar_perfil, name="editar_perfil"),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)