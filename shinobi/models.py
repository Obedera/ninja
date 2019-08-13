from django.db import models

# Create your models here.

#vai cadastrar uma pessoa
class Cadastro(models.Model):
    GENEROS = (
        ('MA', 'Masculino'),
        ('FE', 'Feminino'),
        ('OU', 'Outros'),
    )
    
    nome = models.CharField(
        max_length = 255,
        verbose_name = 'Nome',
    )

    sobrenome = models.CharField(
        max_length = 255,
        verbose_name = 'Sobrenome',
    )

    genero = models.CharField(
        max_length = 25,
        verbose_name = 'Gênero',
        choices=GENEROS,
    )

    email = models.EmailField(
        max_length = 255,
        verbose_name = 'E-mail',
        unique=True
    )
    
    senha = models.CharField(
        max_length = 10,
        verbose_name = 'Senha'
    )

    numero_erros = models.CharField(
        max_length = 255,
        default=0,
        verbose_name = 'Nº de Erros'
    )

    numero_linhas = models.CharField(
        max_length = 255,
        default=0,
        verbose_name = 'Nº de Linhas'
    )

    criacao = models.DateTimeField(auto_now=True)
    ativado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome+' '+self.sobrenome