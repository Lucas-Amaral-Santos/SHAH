
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from django.contrib import messages
from acomodacao.models import Acomodacao
from hospede.models import Hospede
from plataforma.models import Plataforma
from django.contrib.auth.decorators import login_required


def logon(request):
    user_form = UserForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        
        if user_form.is_valid():            
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            messages.warning(request, 'Usuário ou senha incorreta!')
            return redirect('logar')            

    return render(request, 'login.html', {'form':user_form, 'pagina': 'Logue-se'})


def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def home(request):
    try:
        n_acomodacao = Acomodacao.objects.all().__len__()
    except:
        n_acomodacao = 0
    
    try:
        n_hospede = Hospede.objects.all().__len__()
    except:
        n_hospede = 0
    
    try:
        n_plataforma = Plataforma.objects.all().__len__()
    except:
        n_plataforma = 0

    return render(request, 'home.html', {'pagina':'Início', 'n_acomodacao':n_acomodacao, 'n_hospede': n_hospede, 'n_plataforma':n_plataforma})
