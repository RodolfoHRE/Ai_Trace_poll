# votos/models.py
from django.db import models

class UsuarioVotante(models.Model):
    email = models.EmailField(primary_key=True)
    votou_em = models.DateTimeField(auto_now_add=True)

class Imagem(models.Model):
    imagem = models.ImageField(upload_to='imagens/')
    nome = models.CharField(max_length=100)
    fonte = models.CharField(max_length=6)

class Voto(models.Model):
    email = models.ForeignKey(UsuarioVotante, on_delete=models.CASCADE)
    imagem = models.ForeignKey(Imagem, on_delete=models.CASCADE)
    ## Ideias, pode ser alterado
    RESPOSTAS = [('IA', 'IA'), ('HUMANO', 'Humano')]          
    resposta = models.CharField(max_length=6, choices=RESPOSTAS)
    ##