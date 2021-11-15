from django.forms import ModelForm
from app.models import user

# form de usuário.
class userForm(ModelForm):
    class Meta:
        model = user
        fields = ['nome', 'email', 'senha', 'cpf', 'nis', 'pais', 'estado', 'municipio', 'rua', 'cep', 'numero', 'complemento']