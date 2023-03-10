from django.shortcuts import render
from .forms import PlataformaForm, ComissaoForm
from .models import Plataforma, Comissao

# Create your views here.
def cadastra_plataforma(request):
    
    plataforma_form = PlataformaForm()

    if request.method == 'POST':
        plataforma_form = PlataformaForm(request.POST)
        if plataforma_form.is_valid():
            nova_plataforma = plataforma_form.save(commit=False)
            nova_plataforma.cadastrado_por = request.user
            nova_plataforma.save()

    return render(request, 'cadastra.html', {'form': plataforma_form, 'pagina': 'Cadastro de Plataforma'})

def cadastra_comissao(request):
    
    comissao_form = ComissaoForm()

    if request.method == 'POST':
        comissao_form = ComissaoForm(request.POST)
        if comissao_form.is_valid():
            comissao_form.save()

    return render(request, 'cadastra.html', {'form': comissao_form, 'pagina': 'Cadastro de Comissão'})


def pesquisa_plataforma(request):
    try:
        plataformas = Plataforma.objects.all()
    except:
        plataformas = None

    return render(request, 'pesquisa_plataforma.html', {'plataformas': plataformas, 'pagina': 'Pesquisa de Plataformas'}) 

def pesquisa_comissao(request):
    try:
        comissoes = Comissao.objects.all()
    except:
        comissoes = None

    return render(request, 'pesquisa_comissao.html', {'comissoes': comissoes, 'pagina': 'Pesquisa de Comissões'})