from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Portada, Noticia, BotAplication

# Create your views here.
class InicioPageView(TemplateView):
    template_name = "core/home.html"

    # Se sobreescribe el contexto, para inyectar los modelos
    def get_context_data(self, **kwargs):
        context = super(InicioPageView, self).get_context_data(**kwargs)
        context['noticia_list'] = Noticia.objects.all()
        context['portada'] = Portada.objects.first()
        context['bot'] = BotAplication.objects.first()
        return context
