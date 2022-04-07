from csv import list_dialects
from re import search
from django.contrib import admin
from .models import Comentarios, Empleo,Empleo_profesional,Empleo_bajo_nivel

# Register your models here.
class EmpleAdmin(admin.ModelAdmin):
 list_display = ["titulo","category","requisitos","oferta"]
 list_editable = ["requisitos","oferta"]
 search_fields = ["titlulo","category"]
 list_filter = ["requisitos","oferta"]
 list_per_page = 10


class Emple_proAdmin(admin.ModelAdmin):
 list_display = ["titulo","category","requisitos","oferta"]
 list_editable = ["requisitos","oferta"]
 search_fields = ["titlulo","category"]
 list_filter = ["requisitos","oferta"]
 list_per_page = 5


class Emple_bajoAdmin(admin.ModelAdmin):
 list_display = ["titulo","category","requisitos","oferta"]
 list_editable = ["requisitos","oferta"]
 search_fields = ["titlulo","category"]
 list_filter = ["requisitos","oferta"]
 list_per_page = 8

class ComentariosAdmin(admin.ModelAdmin):
 list_display =["nombre", "telefono", "email", "comentario"]
 list_editable = ["cometario"]
 list_per_page = 10

admin.site.register(Empleo, EmpleAdmin)
admin.site.register(Empleo_profesional, Emple_bajoAdmin)
admin.site.register(Empleo_bajo_nivel, Emple_bajoAdmin)
admin.site.register(Comentarios, ComentariosAdmin)