from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Comissao(models.Model):
    comissao = models.FloatField()
    dt_inicio = models.DateField()
    dt_fim = models.DateField()

    def __str__(self):
        return str(self.comissao)


class Plataforma(models.Model):
    nome = models. CharField(max_length=200, verbose_name="Nome da plataforma:")
    mensalidade = models.FloatField(null=True, blank=True)
    comissao = models.ForeignKey(Comissao, on_delete=models.CASCADE, null=True, blank=True)
    
    slug = models.SlugField()
    dt_cadastro = models.DateTimeField(auto_now=True)
    dt_update = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.id)
            super(Comissao, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.nome)
