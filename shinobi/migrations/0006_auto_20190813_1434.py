# Generated by Django 2.2.4 on 2019-08-13 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shinobi', '0005_auto_20190805_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='numero_erros',
            field=models.CharField(default=0, max_length=255, verbose_name='Nº de Erros'),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='numero_linhas',
            field=models.CharField(default=0, max_length=255, verbose_name='Nº de Linhas'),
        ),
    ]
