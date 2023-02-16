from django.forms import ModelForm
from .models import Reserva, Status

class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
        exclude = ['slug', 'dt_cadastro', 'dt_update', 'cadastrado_por']

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = '__all__'
