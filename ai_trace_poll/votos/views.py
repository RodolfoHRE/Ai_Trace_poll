from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from votos.models import Imagem, UsuarioVotante, Voto
from django.db import transaction, IntegrityError
import random

def inicioView(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            try:
                with transaction.atomic():
                    usuario, created = UsuarioVotante.objects.get_or_create(email=email)

                    # Verifica se já existem votos vinculados a esse email
                    if Voto.objects.filter(email=usuario).exists():
                        messages.error(request, 'Este e-mail já participou do questionário.')
                        return redirect('home')

                    # Se acabou de criar ou não tem votos, segue normalmente
                    request.session['email'] = email
                    return redirect('questionario')

            except IntegrityError as e:
                messages.error(request, f'Ocorreu um erro no processamento. Tente novamente. ({str(e)})')
                return redirect('home')

    return render(request, 'inicio.html')





def questionarioView(request):
    email = request.session.get('email')

    if not email:
        messages.error(request, 'Sessão expirada. Insira seu e-mail novamente.')
        return redirect('home')

    usuario = get_object_or_404(UsuarioVotante, email=email)

    if request.method == 'POST':
        imagem_id = request.POST.get('imagem_id')
        resposta = request.POST.get('resposta')

        if not imagem_id or not resposta:
            messages.error(request, 'Resposta inválida. Tente novamente.')
            return redirect('questionario')

        try:
            with transaction.atomic():
                imagem = get_object_or_404(Imagem, id=imagem_id)

                # Verificar se já existe voto para essa imagem e esse usuário (se for necessário)
                if Voto.objects.filter(email=usuario, imagem=imagem).exists():
                    messages.error(request, 'Você já respondeu essa imagem.')
                    return redirect('agradecimento')

                # Criar o voto
                Voto.objects.create(
                    email=usuario,
                    imagem=imagem,
                    resposta=resposta
                )

                return redirect('agradecimento')

        except IntegrityError as e:
            messages.error(request, f'Ocorreu um erro no banco. ({str(e)})')
            return redirect('questionario')

        except Exception as e:
            messages.error(request, f'Ocorreu um erro inesperado. ({str(e)})')
            return redirect('questionario')

    return render(request, 'questionario.html')






def agradecimentoView(request):
    return render(request, 'agradecimento.html')