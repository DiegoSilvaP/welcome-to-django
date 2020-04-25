from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Historia

# Create your views here.
class HistoriaPageView(TemplateView):
    template_name="historia/historia.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['historia'] = Historia.objects.first()
        return context

# Create your views here.
