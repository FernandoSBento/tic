# modulo do django para criar urls
from django.urls import path

# importe todas as suas classes do views.py

from .views import *

urlpatterns = [
    # path (
    # 'caminho/da/url'),
    #  ClasseLaDoView.as_view(), 
    # name="nomeDessaURL"
	path('inicio/', PaginaInicialView.as_view(), name="index"),
    path('sobre/', PaginaSobreView.as_view(), name = "sobre"),
]

