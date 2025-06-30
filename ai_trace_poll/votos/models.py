# votos/models.py
from django.db import models

class UsuarioVotante(models.Model):
    email = models.EmailField(primary_key=True)
    votou_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Imagem(models.Model):
    ORIGEM_CHOICES = (
        ('humano', 'Feita por Humano'),
        ('ia', 'Gerada por IA'),
    )
    IMAGE_CHOICES = (
        ('imagem1', 'Imagem 1'),
        ('imagem2', 'Imagem 2'),
        ('imagem3', 'Imagem 3'),
        ('imagem4', 'Imagem 4'),
        ('imagem5', 'Imagem 5'),
        ('imagem6', 'Imagem 6'),
        ('imagem7', 'Imagem 7'),
        ('imagem8', 'Imagem 8'),
        ('imagem9', 'Imagem 9'),
        ('imagem10', 'Imagem 10'),
    )

    arquivo = models.CharField(max_length=10, choices=IMAGE_CHOICES)
    origem = models.CharField(max_length=10, choices=ORIGEM_CHOICES)

    def __str__(self):
        return f"{self.arquivo} - {self.origem}"

class Voto(models.Model):
    email = models.ForeignKey(UsuarioVotante, on_delete=models.CASCADE)
    imagem = models.ForeignKey(Imagem, on_delete=models.CASCADE)
    ## Ideias, pode ser alterado
    RESPOSTAS = [('IA', 'IA'), ('HUMANO', 'Humano')]          
    resposta = models.CharField(max_length=6, choices=RESPOSTAS)
    ##
    
    def __str__(self):
        return f"{self.email.email} - {self.imagem.arquivo} - {self.resposta}"