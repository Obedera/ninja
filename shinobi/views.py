from django.shortcuts import render
from shinobi.models import Cadastro
from shinobi.leitor_html import analizar_html
from shinobi.leitor_js import analizar_js
from shinobi.leitor_css import analizar_css


# Create your views here.

def index(request):
    if request.method == 'POST':
        if request.POST.get('senha') == request.POST.get('confirmar_senha'):
            usuario = Cadastro()
            usuario.nome = request.POST.get('nome')
            usuario.sobrenome = request.POST.get('sobrenome')
            usuario.genero = request.POST.get('genero')
            usuario.email = request.POST.get('email')
            usuario.senha = request.POST.get('senha')
            usuario.save()
            context = {'msg': 'usuário cadastrado, faça login'}
            return render(request, 'cadastro.html', context)
        else:
            context = {'msg': 'as senhas não correspondem'}
            return render(request, 'cadastro.html', context)
    return render(request, 'cadastro.html')

def login(request):
    if request.method == 'POST':
        email_log = request.POST.get('email')
        validacao = request.POST.get('senha')
        user = Cadastro.objects.filter(email=email_log, senha=validacao).first()
        if user is not None:
            print('verdadeiro')
            context = {'user': user}
            return render(request, 'console.html', context)
        else:
            print('errou')
            context = {'mensag': 'e-mail ou senha incorretos :('}
            return render(request, 'cadastro.html', context)
    return render(request, 'cadastro.html')

def console(request):
    if request.method == 'POST':
        html = analizar_html(request.POST.get('debug'))
        args = {'msg':html}
        
        return render(request, 'console.html', args)
    return render(request, 'console.html',{})