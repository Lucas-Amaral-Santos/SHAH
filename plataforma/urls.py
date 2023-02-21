from django.urls import path, include
from .views import cadastra_plataforma, cadastra_comissao, pesquisa_plataforma, pesquisa_comissao

app_name = 'plataforma'

urlpatterns = [
    path('cadastra_plataforma/', cadastra_plataforma, name='cadastra_plataforma'),
    path('cadastra_comissao/', cadastra_comissao, name='cadastra_comissao'),
    path('pesquisa_plataforma/', pesquisa_plataforma, name='pesquisa_plataforma'),
    path('pesquisa_comissao/', pesquisa_comissao, name='pesquisa_comissao'),
]
