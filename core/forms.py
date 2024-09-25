from django import forms
from .models import Produto 

class ProdutosModelForm(forms.ModelForm): #serve para interface.
    class Meta:
        model = Produto
        fields = ['codigo', 'nome', 'descricao', 'valor', 'imagem']