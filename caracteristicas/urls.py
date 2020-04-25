from django.urls import path
from .views import CaracteristicasListPage,CaracteristicaCreate, CaracteristicaUpdate, CaracteristicaDelete

app_name="caracteristicas"
urlpatterns = [
    path('', CaracteristicasListPage.as_view(), name='lista'),
    path('agregar/', CaracteristicaCreate.as_view(), name='agregar'),
    path('modificar/<int:pk>', CaracteristicaUpdate.as_view(), name='modificar'),
    path('eliminar/<int:pk>', CaracteristicaDelete.as_view(), name='eliminar'),
]
