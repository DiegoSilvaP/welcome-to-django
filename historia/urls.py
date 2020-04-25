from django.urls import path
from .views import HistoriaPageView


urlpatterns = [
    path('', HistoriaPageView.as_view(), name='historia'),
]