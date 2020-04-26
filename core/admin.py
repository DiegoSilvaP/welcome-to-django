from django.contrib import admin
from .models import Portada, Noticia, BotAplication

# Register your models here.

class NoticiaTabularInline(admin.TabularInline):
# class NoticiaTabularInline(admin.StackedInline):
    model = Noticia
    extra =1

class PortadaAdmin(admin.ModelAdmin):
    inlines = [NoticiaTabularInline]
    list_display = ('title','subtitle','link','link_text','updated', 'created')
    list_display_links=('title', 'subtitle')
    list_editable = ('link','link_text')
    class meta:
        model = Portada


class BotAplicationAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display = ('name','endpoint','width','height','updated','created',)
    list_editable = ('endpoint',)


# admin.site.register(Noticia)
admin.site.register(BotAplication,BotAplicationAdmin)
admin.site.register(Portada, PortadaAdmin)
