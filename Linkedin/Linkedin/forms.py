from django import forms
from .models import projetosModel
from .models import contatoModel

class projetosForm(forms.ModelForm):
    class Meta:
        model = projetosModel
        fields = ['titulo', 'descricao', 'tecnologia','repositorio','link']

class contatoForm(forms.ModelForm): 
    class Meta:
        model = contatoModel
        fields = ['nome', 'numero', 'email' , 'mensagem']
