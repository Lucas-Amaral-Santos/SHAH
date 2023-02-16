from django.db import models
from acomodacao.models import Acomodacao
from plataforma.models import Plataforma, Comissao
from hospede.models import Hospede
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Status(models.Model):
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status

class Reserva(models.Model):

    acomodacao = models.ForeignKey(Acomodacao, on_delete=models.CASCADE)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    comissao = models.ForeignKey(Comissao, on_delete=models.CASCADE)
    hospede = models.ForeignKey(Hospede, on_delete=models.CASCADE)
    dt_inicio = models.DateField()
    dt_fim = models.DateField() 
    status  = models.ForeignKey(Status, on_delete=models.CASCADE)

    slug = models.SlugField()
    dt_cadastro = models.DateTimeField(auto_now=True)
    dt_update = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.id)
            super(Reserva, self).save(*args, **kwargs)


    def __str__(self):
        return self.nome