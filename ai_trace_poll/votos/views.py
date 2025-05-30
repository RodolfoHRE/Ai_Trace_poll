from django.shortcuts import render
from votos.models import Imagem
import random


def inicioView(request):
    return render(request, 'inicio.html')

def questionarioView(request):

    imagens = Imagem.objects.all().order_by('id')[:1]  # Apenas uma imagem por enquanto
    return render(request, 'questionario.html', {'imagens': imagens})