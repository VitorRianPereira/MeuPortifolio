from django.db import models


class projetosModel(models.Model):
    titulo = models.CharField(max_length = 150)
    descricao = models.TextField(max_length= 200000)
    tecnologia = models.CharField(max_length = 100)
    repositorio = models.CharField(max_length = 300, blank = True)
    link = models.CharField(max_length = 300, blank=True)
    data = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return self.titulo

class contatoModel(models.Model):
    nome = models.CharField(max_length = 150)
    numero = models.CharField(max_length = 30)
    email = models.TextField(max_length = 300)
    mensagem = models.TextField(max_length = 3000000)
    data = models.DateTimeField(auto_now_add= True)
