from django.db import models

# modelo de usuário.
class user(models.Model):

    nome = models.CharField(max_length=30,blank=True, null=True)
    email = models.EmailField(max_length=45,blank=True, null=True)
    senha = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.DecimalField(max_digits=11, decimal_places=0, default='', blank=True, null=True)
    nis = models.DecimalField(max_digits=11, decimal_places=0, default='', blank=True, null=True)
    pais= models.CharField(max_length=30,  blank=True, null=True)
    estado = models.CharField(max_length=45,  blank=True, null=True)
    municipio = models.CharField(max_length=100, blank=True, null=True)
    rua = models.CharField(max_length=30,  blank=True, null=True)
    cep = models.DecimalField(max_digits=8, decimal_places=0, default='',  blank=True, null=True)
    numero = models.DecimalField(max_digits=10, decimal_places=0, default='', blank=True, null=True)
    complemento = models.CharField(max_length=30, blank=True, null=True)



