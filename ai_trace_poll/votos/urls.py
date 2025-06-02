
from django.urls import path, include
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.inicioView, name='home'),
    path('questionario', views.questionarioView, name='questionario'),
    path('agradecimento', views.agradecimentoView, name='agradecimento'),
]