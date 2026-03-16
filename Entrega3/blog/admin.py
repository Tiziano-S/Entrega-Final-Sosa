from django.contrib import admin
from .models import Publicacion

@admin.register(Publicacion)
class PostAdmin(admin.ModelAdmin):
    list_display = ["titulo","estado","autor","fecha_publicacion"]
    list_filter = ["autor","estado"]
    raw_id_fields = ["autor"]
    ordering = ["-fecha_publicacion"]