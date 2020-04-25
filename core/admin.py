from django.contrib import admin
from .models import Portada, Noticia, BotAplication

# Register your models here.

class NoticiaTabularInline(admin.TabularInline):
    model = Noticia
    extra =1

class PortadaAdmin(admin.ModelAdmin):
    inlines = [NoticiaTabularInline]
    list_display = ('title','subtitle','updated','created',)
    search_fields = ['title','subtitle']
    list_filter = ('title',)
    class meta:
        model = Portada


class BotAplicationAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display = ('name','endpoint','width','height','updated','created',)
    list_editable = ('endpoint',)

admin.site.register(BotAplication,BotAplicationAdmin)
admin.site.register(Portada, PortadaAdmin)
