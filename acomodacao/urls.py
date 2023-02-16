from django.urls import path, include
from .views import cadastra_proprietario, cadastra_acomodacao, pesquisa_acomodacao, cadastra_servico, pesquisa_proprietario

app_name = 'acomodacao'

urlpatterns = [
    path('cadastra_acomodacao/', cadastra_acomodacao, name='cadastra_acomodacao'),
    path('cadastra_proprietario/', cadastra_proprietario, name='cadastra_proprietario'),
    path('cadastra_servico/', cadastra_servico, name='cadastra_servico'),
    path('pesquisa_acomodacao/', pesquisa_acomodacao, name='pesquisa_acomodacao'),
    path('pesquisa_proprietario/', pesquisa_proprietario, name='pesquisa_proprietario'),
    path('pesquisa_proprietario/', pesquisa_proprietario, name='pesquisa_proprietario'),
]
