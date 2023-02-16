from django.shortcuts import render
from .forms import ReservaForm, StatusForm

def cadastra_reserva(request):
    
    reserva_form = ReservaForm()

    if request.method == 'POST':
        reserva_form = ReservaForm(request.POST)
        if reserva_form.is_valid():
            reserva_form.save()

    return render(request, 'cadastra.html', {'form': reserva_form, 'pagina': 'Cadastro de Reserva'})

def cadastra_status(request):
    
    status_form = StatusForm()

    if request.method == 'POST':
        status_form = StatusForm(request.POST)
        if status_form.is_valid():
            status_form.save()

    return render(request, 'cadastra.html', {'form': status_form, 'pagina': 'Cadastro de Status'})