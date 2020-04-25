from django.contrib import admin
from .models import Caracteristica
from django.utils.html import format_html

# Register your models here.
class CaracteristicaAdmin(admin.ModelAdmin):
    # Qué campos mostrar en la lista de registros
    list_display = ('name','descripción_corta','created','updated','eliminar')
    # Cuáles de esos campos pueden ser links para acceder a dicho registro
    list_display_links=('name','descripción_corta')
    # Qué campos se pueden utilizar para filtrar
    list_filter = ('name','created','updated')
    # A través de qué campos se puede buscar
    search_fields = ('name','description')

    # Creamos botón para eliminar y lo insertamos en cada fila
    def eliminar(self, obj):
        return format_html('<a class="deletelink" href="/admin/caracteristicas/caracteristica/{}/delete/">Eliminar</a>', obj.id)

    # Personalizamos el cómo mostrar la descripción
    def descripción_corta(self, obj):
        # Se regresan 100 caracteres
        return f"{obj.description[:100]}..."


admin.site.register(Caracteristica, CaracteristicaAdmin)
