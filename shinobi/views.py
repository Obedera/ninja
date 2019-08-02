from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'cadastro.html')

def console(request):
    return render(request, 'console.html')