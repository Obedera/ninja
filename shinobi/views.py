import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from shinobi.models import Cadastro
from shinobi.leitor_html import analizar_html
from shinobi.leitor_js import analizar_js
from shinobi.leitor_css import analizar_css
from shinobi.chat import analizar_resposta


# Create your views here.

def index(request):
    context = {}
    if request.method == 'POST':
        email_user = request.POST.get('email')
        pessoa_bd = Cadastro.objects.filter(email=email_user)
        
        if str(pessoa_bd) != '<QuerySet []>':
            context = {'msg':'Email já cadastrado'}
            return render(request, 'cadastro.html', context)
        else:
            if request.POST.get('senha') != request.POST.get('confirmar_senha'):
                context = {'msg': 'As senhas não correspondem'}
                return render(request, 'cadastro.html', context)
            else:
                usuario = Cadastro()
                usuario.nome = request.POST.get('nome')
                usuario.sobrenome = request.POST.get('sobrenome')
                usuario.genero = request.POST.get('genero')
                usuario.email = request.POST.get('email')
                usuario.senha = request.POST.get('senha')
                usuario.save()
                context = {'msg': 'usuário cadastrado, faça login'}
                return render(request, 'cadastro.html', context)

    return render(request, 'cadastro.html', context)

def login(request):
    if request.method == 'POST':
        email_log = request.POST.get('email')
        validacao = request.POST.get('senha')
        user = Cadastro.objects.filter(email=email_log, senha=validacao).first()
        if user is not None:
           
            context = {'user': user}
            return render(request, 'console.html', context)
        else:
            context = {'mensag': 'e-mail ou senha incorretos :('}
            return render(request, 'cadastro.html', context)
    return render(request, 'cadastro.html')

def console(request):
    if request.method == 'POST':
        texto_convertido = json.loads(request.POST.get('json'))
        emailUser = texto_convertido['email']
        senhaUser = texto_convertido['senha']
        user = Cadastro.objects.filter(email=emailUser, senha=senhaUser).first()
        if user is not None:
            linhas_bd = int(user.numero_linhas)
            erros_bd = int(user.numero_erros)
            linhas = len(texto_convertido['texto'].split('\n'))
            
            if texto_convertido['linguagem'] == 'H':
                erros = analizar_html(texto_convertido['texto'])
                
            if texto_convertido['linguagem'] == 'J':
                erros = analizar_js(texto_convertido['texto'])
        
            if texto_convertido['linguagem'] == 'C':
                erros = analizar_css(texto_convertido['texto'])

            user.numero_linhas = str(linhas+linhas_bd)
            print(user.numero_linhas)
            print(erros[1]) 
            return JsonResponse({'texto':erros[0]}, status=200)
        return JsonResponse({'texto':'Você não está logado'}, status=200)

    return render(request, 'console.html',{})


        
def chat(request):
    if request.method == 'POST':
        texto_convertido = json.loads(request.POST.get('json'))
        resposta = analizar_resposta(texto_convertido['texto'])
        return JsonResponse({'texto':resposta}, status=200)
    return render(request, 'console.html',{})
