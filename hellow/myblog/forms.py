from django import forms

from .models import usuario

class Usuariosapp(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['nome', 'email', 'assunto', 'mensagem']

