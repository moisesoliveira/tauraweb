from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.
from django.views.generic import CreateView, UpdateView
from membros.models import Membro

class CriaMembro(CreateView):
    model = Membro
    fields = ['first_name', 'last_name', 'email', 'username', 'password', 'area_de_atuacao']
    template_name = 'criar-membro.html'
    success_url = '.'

 #Adiciona um password criptografado para o usuario
    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.set_password(form.cleaned_data['password'])
        usuario.save()
        return super(CriaMembro, self).form_valid(form)

def membros(request):
    membros = Membro.objects.all()
    return render(request, 'membros.html', {'membros': membros})

def membro(request, id=None):
    membro = get_object_or_404(Membro, id=id)
    return render(request, 'membro.html', {'membro': membro})

@login_required
def excluir(request, id=None):
    membro = get_object_or_404(Membro, id=id)
    membro.delete()
    return redirect(membros)

def logar(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user) # Salva o usuario na session atual
            return redirect("membros")
        else:
            return render(request, 'login.html')
    else: # GET apenas carrega a pagina
        return render(request, 'login.html')

def sair(request):
    return render(request, 'login.html')