import os
import sys
import django
import csv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Ajuste o caminho do DJANGO_SETTINGS_MODULE conforme seu projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_trace_poll.settings')
django.setup()

from votos.models import UsuarioVotante, Imagem, Voto


# Cria a pasta resultado se não existir
RESULTADO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'resultado')
os.makedirs(RESULTADO_DIR, exist_ok=True)

# Exporta UsuarioVotante
with open(os.path.join(RESULTADO_DIR, 'usuarios.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['email', 'votou_em'])
    for u in UsuarioVotante.objects.all():
        writer.writerow([u.email, u.votou_em])

# Exporta Imagem
with open(os.path.join(RESULTADO_DIR, 'imagens.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'arquivo', 'origem'])
    for img in Imagem.objects.all():
        writer.writerow([img.id, img.arquivo.name if img.arquivo else '', img.origem])

# Exporta Voto
with open(os.path.join(RESULTADO_DIR, 'votos.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'email', 'imagem_id', 'resposta'])
    for v in Voto.objects.all():
        writer.writerow([v.id, v.email.email, v.imagem.id, v.resposta])

print("Exportação concluída! Arquivos salvos na pasta resultado/")