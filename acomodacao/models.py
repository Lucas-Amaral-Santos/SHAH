from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Servico(models.Model):
    nome = models.CharField(max_length=200)
    tx_servico = models.FloatField()
    descricao = models.TextField(null=True, blank=True)  

    def __str__(self):
        return self.nome


class Proprietario(models.Model):
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)
    mei = models.CharField(max_length=18)
    cep = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)    
    
    slug = models.SlugField()
    dt_cadastro = models.DateTimeField(auto_now=True)
    dt_update = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.id)
            super(Proprietario, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

class Acomodacao(models.Model):
    nome = models.CharField(max_length=200)
    cep = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE)

    slug = models.SlugField()
    dt_cadastro = models.DateTimeField(auto_now=True)
    dt_update = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.id)
            super(Acomodacao, self).save(*args, **kwargs)


    def __str__(self):
        return self.nome
    