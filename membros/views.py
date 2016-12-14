from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.views.generic import CreateView, UpdateView
from membros.models import Membro
from django.contrib.auth import authenticate, login

class CriaMembro(CreateView):
    model = Membro
    fields = ['first_name', 'last_name', 'email', 'username', 'password','matricula']
    template_name = 'criar-membro.html'
    success_url = '.'

    # Adiciona um password criptografado para o usuario
#    def form_valid(self, form):
#        usuario = form.save(commit=False)
#        usuario.set_password(form.cleaned_data['password'])
#        usuario.save()
#        return super(CriaMembro, self).form_valid(form)

def membros(request):
    membros = Membro.objects.all()
    return render(request, 'membros.html', {'membros': membros})

def membro(request, id=None):
    membro = get_object_or_404(Membro, id=id)
    return render(request, 'membro.html', {'membro': membro})