from django.shortcuts import render, redirect
from django.contrib import messages
from votos.models import Imagem, UsuarioVotante, Voto
import random


def inicioView(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            # Verificar se o e-mail já existe no banco
            if UsuarioVotante.objects.filter(email=email).exists():
                usuario = UsuarioVotante.objects.get(email=email)

                if Voto.objects.filter(email=usuario).exists():
                    messages.error(request, 'Este e-mail já participou do questionário.')
                    return redirect('home')
                
                else:
                    request.session['email'] = email
                    return redirect('questionario')
            else:
                # Se não existe, salva e segue para o questionário
                UsuarioVotante.objects.create(email=email)
                request.session['email'] = email
                return redirect('questionario')

    return render(request, 'inicio.html')





def questionarioView(request):
    email = request.session.get('email')

    if not email:
        messages.error(request, 'Sessão expirada. Insira seu e-mail novamente.')
        return redirect('home')

    usuario = UsuarioVotante.objects.get(email=email)

    if request.method == 'POST':
        imagem_id = request.POST.get('imagem_id')
        resposta = request.POST.get('resposta')

        if not imagem_id or not resposta:
            messages.error(request, 'Resposta inválida. Tente novamente.')
            return redirect('questionario')


        ## fazer igual no bonds, atomic try ou algo assim, mas para o create todo e com vários pontos para log de erro
        try:
            imagem = Imagem.objects.get(id=imagem_id)
        except Imagem.DoesNotExist:
            messages.error(request, 'Imagem inválida.')
            return redirect('questionario')

        Voto.objects.create(
            email=usuario,
            imagem=imagem,
            resposta=resposta
        )

        return redirect('agradecimento')

    return render(request, 'questionario.html')






def agradecimentoView(request):
    return render(request, 'agradecimento.html')