#  AI Trace – Site de Votação de Imagens Geradas por IA

Este repositório contém o código do site de votação utilizado no projeto de TCC **"AI Trace"**, que propõe um estudo sobre a geração de imagens por inteligência artificial e o julgamento humano sobre sua autenticidade ou qualidade visual.

##  Objetivo

Permitir que usuários visualizem imagens geradas por IA e façam votações baseadas em critérios como:

- Qualidade visual
- Realismo
- Preferência pessoal

Os dados das votações são utilizados para análises posteriores no contexto do TCC.

## Tecnologias utilizadas

- **Django** (backend e templates)
- **HTML + CSS** (frontend simples)
- **SQLite** (banco de dados padrão do Django)
- (Em breve) **TailwindCSS** ou **Bootstrap** para estilização

## Estrutura do Projeto

```bash
ai_trace/
│
├── votacao/              # App principal (votação)
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── ai_trace/             # Configuração principal do Django
│
├── manage.py
└── README.md
