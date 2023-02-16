from django.urls import path, include
from .views import cadastra_reserva, cadastra_status

app_name = 'reserva'

urlpatterns = [
    path('cadastra_reserva/', cadastra_reserva, name='cadastra_reserva'),
    path('cadastra_status/', cadastra_status, name='cadastra_status'),
]
