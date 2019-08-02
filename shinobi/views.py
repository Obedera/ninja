from django.shortcuts import render
# from leitor_html import analizar_html
# from leitor_js import analizar_js
# from leitor_css import analizar_css


# Create your views here.

def index(request):
    return render(request, 'cadastro.html')

def console(request):
    if request.method == 'POST':
        html = request.POST.get('debug')
        print(html)
        args = {'msg':html}
        return render(request, 'console.html', args)
    return render(request, 'console.html',{})