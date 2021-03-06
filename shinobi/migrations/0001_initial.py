# Generated by Django 2.2.4 on 2019-08-04 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('Sobrenome', models.CharField(max_length=255, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('senha', models.CharField(max_length=10, verbose_name='Senha')),
                ('confirmar_senha', models.CharField(max_length=10, verbose_name='Confirmar Senha')),
                ('criacao', models.DateTimeField(auto_now=True)),
                ('ativado', models.BooleanField(default=True)),
            ],
        ),
    ]
