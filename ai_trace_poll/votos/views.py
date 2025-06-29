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
    total_imagens = 10  # Atualize conforme o número de imagens

    if request.method == 'POST':
        votos = []
        for i in range(1, total_imagens + 1):
            imagem_id = request.POST.get(f'imagem_id_{i}')
            resposta = request.POST.get(f'resposta_{i}')
            if imagem_id and resposta:
                votos.append((imagem_id, resposta))

        if not votos:
            messages.error(request, 'Nenhuma resposta foi enviada. Tente novamente.')
            return redirect('questionario')

        try:
            with transaction.atomic():
                for imagem_id, resposta in votos:
                    imagem = get_object_or_404(Imagem, id=imagem_id)
                    if not Voto.objects.filter(email=usuario, imagem=imagem).exists():
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
    email = request.session.get('email')
    acertos = 0
    total = 0
    percentual = None
    if email:
        usuario = get_object_or_404(UsuarioVotante, email=email)
        votos = Voto.objects.filter(email=usuario)
        total = votos.count()
        for voto in votos:
            if (voto.resposta == 'HUMANO' and voto.imagem.origem == 'humano') or (voto.resposta == 'IA' and voto.imagem.origem == 'ia'):
                acertos += 1
        if total > 0:
            percentual = round((acertos / total) * 100)
    return render(request, 'agradecimento.html', {'percentual': percentual, 'acertos': acertos, 'total': total})