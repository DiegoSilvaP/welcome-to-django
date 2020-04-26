from django.contrib import admin
from .models import Caracteristica
from django.utils.html import format_html

# Register your models here.
class CaracteristicaAdmin(admin.ModelAdmin):
    # Qué campos mostrar en la lista de registros
    list_display = ('name','print_short_description','created','updated','remove_button')
    # Cuáles de esos campos pueden ser links para acceder a dicho registro
    list_display_links=('name','print_short_description')
    # Qué campos se pueden utilizar para filtrar
    list_filter = ('name','created','updated')
    # A través de qué campos se puede buscar
    search_fields = ('name','description')

    # Creamos botón para eliminar y lo insertamos en cada fila
    def remove_button(self, obj):
        return format_html('<a class="deletelink" href="/admin/caracteristicas/caracteristica/{}/delete/">Eliminar</a>', obj.id)
    remove_button.short_description = "Acción"

    # Personalizamos el cómo mostrar la descripción
    def print_short_description(self, obj):
        # Se regresan 100 caracteres
        return f"{obj.description[:100]}..."
    print_short_description.short_description = "Descripción"
    print_short_description.admin_order_field = "name"
        


admin.site.register(Caracteristica, CaracteristicaAdmin)
