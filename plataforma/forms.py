from django.forms import ModelForm
from .models import Plataforma, Comissao

class PlataformaForm(ModelForm):
    class Meta:
        model = Plataforma
        fields = '__all__'
        exclude = ['slug', 'dt_cadastro', 'dt_update', 'cadastrado_por']

class ComissaoForm(ModelForm):
    class Meta:
        model = Comissao
        fields = '__all__'
