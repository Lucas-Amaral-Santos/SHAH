from django.forms import ModelForm
from .models import Acomodacao, Proprietario, Servico

class AcomodacaoForm(ModelForm):
    class Meta:
        model = Acomodacao
        fields = '__all__'
        exclude = ['slug', 'dt_cadastro', 'dt_update', 'cadastrado_por']


class ProprietarioForm(ModelForm):
    class Meta:
        model = Proprietario
        fields = '__all__'
        exclude = ['slug', 'dt_cadastro', 'dt_update', 'cadastrado_por']

class ServicoForm(ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'
