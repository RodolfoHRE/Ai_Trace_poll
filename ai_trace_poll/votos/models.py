# votos/models.py
from django.db import models

class UsuarioVotante(models.Model):
    email = models.EmailField(primary_key=True)
    votou_em = models.DateTimeField(auto_now_add=True)

class Imagem(models.Model):
    ORIGEM_CHOICES = (
        ('humano', 'Feita por Humano'),
        ('ia', 'Gerada por IA'),
    )
    arquivo = models.ImageField(upload_to='imagens/')
    origem = models.CharField(max_length=10, choices=ORIGEM_CHOICES)

class Voto(models.Model):
    email = models.ForeignKey(UsuarioVotante, on_delete=models.CASCADE)
    imagem = models.ForeignKey(Imagem, on_delete=models.CASCADE)
    ## Ideias, pode ser alterado
    RESPOSTAS = [('IA', 'IA'), ('HUMANO', 'Humano')]          
    resposta = models.CharField(max_length=6, choices=RESPOSTAS)
    ##