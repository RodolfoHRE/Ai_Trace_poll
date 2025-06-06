# Generated by Django 5.2.1 on 2025-05-29 19:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.ImageField(upload_to='imagens/')),
                ('origem', models.CharField(choices=[('humano', 'Feita por Humano'), ('ia', 'Gerada por IA')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioVotante',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('votou_em', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.CharField(choices=[('IA', 'IA'), ('HUMANO', 'Humano')], max_length=6)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votos.usuariovotante')),
                ('imagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votos.imagem')),
            ],
        ),
    ]
