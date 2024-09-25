from django.db import models
from stdimage.models import StdImageField

# Create your models here.

class Produto(models.Model):
    codigo = models.IntegerField('Codigo do Produto', blank=False, primary_key=True, unique=True, auto_created=True) #interegerField = int
    nome = models.CharField('Nome do Produto', max_length=100, blank=False)
    descricao = models.CharField('Descrição', max_length=100, blank=False)
    valor = models.DecimalField('Valor do produto',max_digits=10, decimal_places=2)
    imagem = StdImageField('Imagem do Produto', variations={'thumb': (124,124)}) #largura e altura
 
    def __str__(self):
        return self.nome

#quando criar uma pasta no models, dar makemigrations.