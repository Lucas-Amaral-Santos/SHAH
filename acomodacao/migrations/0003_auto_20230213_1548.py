# Generated by Django 3.2.17 on 2023-02-13 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acomodacao', '0002_auto_20230212_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('tx_servico', models.FloatField()),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=14)),
                ('mei', models.CharField(max_length=18)),
                ('cep', models.CharField(max_length=200)),
                ('endereco', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=200)),
                ('complemento', models.CharField(max_length=200)),
                ('bairro', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('dt_cadastro', models.DateTimeField(auto_now=True)),
                ('dt_update', models.DateTimeField(auto_now=True)),
                ('cadastrado_por', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='acomodacao',
            name='proprietario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='acomodacao.proprietario'),
            preserve_default=False,
        ),
    ]
