from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>hello {} de {} anos</h1>'.format(nome, idade))

def soma(request, valor1, valor2):
    soma = valor1 + valor2
    return HttpResponse('a soma foi de {}'.format(soma))