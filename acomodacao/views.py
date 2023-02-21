from django.shortcuts import render, redirect
from .forms import AcomodacaoForm, ProprietarioForm, ServicoForm
from .models import Acomodacao, Proprietario

def pesquisa_acomodacao(request):
    try:
        acomodacoes = Acomodacao.objects.all()
    except:
        acomodacoes = None

    return render(request, 'pesquisa_acomodacao.html', {'acomodacoes': acomodacoes, 'pagina': 'Pesquisar Acomodações'})

def pesquisa_proprietario(request):
    try:
        proprietarios = Proprietario.objects.all()
    except:
        proprietarios = None

    return render(request, 'pesquisa_proprietario.html', {'proprietarios': proprietarios, 'pagina': 'Pesquisar Proprietários'})



def cadastra_proprietario(request):
    
    proprietario_form = ProprietarioForm()

    if request.method == 'POST':
        proprietario_form = ProprietarioForm(request.POST)
        if proprietario_form.is_valid():
            novo_proprietario = proprietario_form.save(commit=False)
            novo_proprietario.cadastrado_por = request.user
            novo_proprietario.save()
            return redirect('/')
    return render(request, 'cadastra.html', {'form': proprietario_form, 'pagina': 'Cadastro de Proprietário'})


def cadastra_acomodacao(request):
    
    acomodacao_form = AcomodacaoForm()

    if request.method == 'POST':
        acomodacao_form = AcomodacaoForm(request.POST)
        if acomodacao_form.is_valid():
            nova_acomodacao = acomodacao_form.save(commit=False)
            nova_acomodacao.cadastrado_por = request.user
            nova_acomodacao.save()
            return redirect('acomodacao:pesquisa_acomodacao')

    return render(request, 'cadastra.html', {'form': acomodacao_form, 'pagina': 'Cadastro de Acomodação'})

def cadastra_servico(request):
    
    servico_form = ServicoForm()

    if request.method == 'POST':
        servico_form = ServicoForm(request.POST)
        if servico_form.is_valid():
            novo_servico = servico_form.save(commit=False)
            novo_servico.cadastrado_por = request.user
            novo_servico.save()
            return redirect('/')
    return render(request, 'cadastra.html', {'form': servico_form, 'pagina': 'Cadastro de Serviço'})