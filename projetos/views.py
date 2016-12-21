from django.shortcuts import render
# Create your views here.
from .models import Projeto
from django.views.generic import CreateView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


class IncluirProjeto(CreateView):
    model = Projeto
    fields = ['titulo','descricao','responsavel']
    template_name = 'inclur-projeto.html'
    success_url = '.'

def projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos.html', {'projetos': projetos})


def projeto(request, id=None):
    projeto = get_object_or_404(Projeto, id=id)
    return render(request, 'projeto.html', {'projeto': projeto})

@login_required
def excluir(request, id=None):
    projeto = get_object_or_404(Projeto, id=id)
    projeto.delete()
    return redirect(projetos)