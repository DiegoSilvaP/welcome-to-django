from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Caracteristica
from .forms import CaracteristicaForm

# Proteger vistas de usuarios no logueados
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

# Create your views here.
class CaracteristicasListPage(ListView):
    model = Caracteristica

# Nos sirve para validar que el usuario logueado sea staff
@method_decorator(staff_member_required, name='dispatch')
class CaracteristicaCreate(CreateView):
    model = Caracteristica
    form_class = CaracteristicaForm
    # Sobreescribimos el metodo get_success_url para que nos redirija automaticamente a la publicacion creada por medio del ID y del SLUG
    def get_success_url(self):
        # print("ID:",self.object.id, "Slug:",slugify(self.object.name))
        return reverse_lazy('caracteristicas:lista')

@method_decorator(staff_member_required, name='dispatch')
class CaracteristicaUpdate(UpdateView):
    model = Caracteristica
    form_class = CaracteristicaForm
    # El sufijo se establece, para que vaya a buscar el template, de lo contrario iria a buscar el template de creacion
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('caracteristicas:lista')


@method_decorator(staff_member_required, name='dispatch')
class CaracteristicaDelete(DeleteView):
    model = Caracteristica
    success_url = reverse_lazy('caracteristicas:lista')
