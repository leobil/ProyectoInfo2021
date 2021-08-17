from django.contrib import admin

# Register your models here.
from .models import Pregunta, Respuesta, Partida, Categoria

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'id_categoria','autor')

class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('id_pregunta', 'opcion', 'puntaje')

class PartidaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha', 'resultado')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'descripcion')

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta, RespuestaAdmin)
admin.site.register(Partida, PartidaAdmin)
admin.site.register(Categoria, CategoriaAdmin)

