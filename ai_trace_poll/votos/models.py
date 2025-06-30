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


    arquivo = models.CharField(max_length=50, null=False)
    origem = models.CharField(max_length=10, choices=ORIGEM_CHOICES, null=False)

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