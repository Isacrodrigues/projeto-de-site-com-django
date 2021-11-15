from django.shortcuts import redirect, render
from app.models import user
from app.forms import userForm



# view para a home.
def home(request) :
    data = {}
    data['db'] = user.objects.all()
    return render(request, 'index.html', data)


# view para formulário.
def form(request) :
    data = {}
    data['form'] = userForm()
    return render(request, "formulario.html", data)


# view para criar um novo usuário. 
def create(request) :
    form = userForm(request.POST or None)
    if form.is_valid() :
        form.save()
        return redirect('/')


#view para retornar uma página com as tabelas de usuários.
def users(request) :
    data = {}
    data['db'] = user.objects.all()
    return render(request, "Users.html", data)


#view para retornar uma página com os dados de um usuário específico.
def view(request, pk) :
    data = {}
    data['db'] = user.objects.get(pk=pk)
    return render(request, "view.html", data)


#view para página de editar um usuário
def edit(request, pk) :
    data = {}
    data['db'] = user.objects.get(pk=pk)
    data['form'] = userForm(instance=data['db'])
    return render(request, "formulario.html", data)


#view para enviar o update para o banco.
def update(request, pk) :
    data = {}
    data['db'] = user.objects.get(pk=pk)
    form = userForm(request.POST or None, instance=data['db'])    
    if form.is_valid() :
        form.save()
        return redirect("users")


#view para deletar um usuário o banco.
def delete(request, pk) :
    db= user.objects.get(pk=pk)
    db.delete()
    return redirect("users")






