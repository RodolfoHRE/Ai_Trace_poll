import sys
import os
import django
import argparse

# Adiciona o diretório do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_trace_poll.settings')
django.setup()

from votos.models import Voto

parser = argparse.ArgumentParser(description="Atualiza o campo 'acertou' dos votos antigos.")
parser.add_argument('--apply', action='store_true', help='Se definido, aplica as alterações no banco de dados.')
args = parser.parse_args()

apply = args.apply

total_atualizados = 0

for voto in Voto.objects.filter(acertou__isnull=True).select_related('imagem'):
    acertou = (
        (voto.resposta == 'HUMANO' and voto.imagem.origem == 'humano') or
        (voto.resposta == 'IA' and voto.imagem.origem == 'ia')
    )
    print(f"Voto id={voto.id}: resposta={voto.resposta}, origem={voto.imagem.origem}, acertou={acertou}")
    if apply:
        voto.acertou = acertou
        voto.save(update_fields=['acertou'])
        total_atualizados += 1

if apply:
    print(f"Atualizados {total_atualizados} votos com o campo 'acertou'.")
else:
    print("Modo simulação: Nenhum voto foi alterado. Use --apply para atualizar o banco.")