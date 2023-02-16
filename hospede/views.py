from django.shortcuts import render, redirect
from .models import Hospede
from .forms import HospedeForm

def pesquisa_hospede(request):
    try:
        hospedes = Hospede.objects.all()
    except:
        hospedes = None

    return render(request, 'pesquisa_hospede.html', {'hospedes': hospedes, 'pagina': 'Pesquisar Hóspedes'})

def cadastra_hospede(request):

    hospede_form = HospedeForm()

    if request.method == 'POST':
        hospede_form = HospedeForm(request.POST)
        if hospede_form.is_valid():
            novo_hospede = hospede_form.save(commit=False)
            novo_hospede.cadastrado_por = request.user
            novo_hospede.save()
            return redirect("hospede:pesquisa_hospede")


    return render(request, 'cadastra.html', {'form': hospede_form, 'pagina': 'Cadastro de Hóspede'})