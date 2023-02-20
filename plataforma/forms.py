from django.forms import ModelForm, CheckboxInput, BooleanField, FloatField, NumberInput, DateField
from .models import Plataforma, Comissao

class PlataformaForm(ModelForm):
    class Meta:
        model = Plataforma
        fields = '__all__'
        exclude = ['slug', 'dt_cadastro', 'dt_update', 'cadastrado_por']

class ComissaoForm(ModelForm):
    comissao = FloatField(label="Comissão (R$)", required=True)
    comissao_vigente = BooleanField(widget=CheckboxInput, required=True)
    dt_inicio = DateField(widget=NumberInput(attrs={'type':'date'}), required=True, label="Data de inicio da vigência:")
    dt_fim = DateField(widget=NumberInput(attrs={'type':'date'}), required=False, label="Data de fim da vigência:")
    class Meta:
        model = Comissao
        fields = ['comissao', 'plataforma', 'dt_inicio', 'comissao_vigente', 'dt_fim']
