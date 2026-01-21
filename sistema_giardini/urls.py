from django.contrib import admin
from django.urls import path
from reservas.views import criar_reserva  # <--- IMPORTANTE: Importar a view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', criar_reserva, name='home'), # <--- Deixei na página inicial (vazio)
]