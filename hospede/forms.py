from django.forms import ModelForm
from .models import Hospede

class HospedeForm(ModelForm):
    class Meta:
        model = Hospede
        fields = '__all__'
        exclude = ['slug', 'dt_cadastro', 'dt_update', 'cadastrado_por']