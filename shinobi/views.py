from django.shortcuts import render
from shinobi.leitor_html import analizar_html
from shinobi.leitor_js import analizar_js
from shinobi.leitor_css import analizar_css


# Create your views here.

def index(request):
    return render(request, 'cadastro.html')

def console(request):
    if request.method == 'POST':
        html = analizar_html(request.POST.get('debug'))
        args = {'msg':html}
        
        return render(request, 'console.html', args)
    return render(request, 'console.html',{})