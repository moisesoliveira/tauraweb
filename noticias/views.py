from django.shortcuts import render
# Create your views here.
from .models import Noticia
from django.views.generic import CreateView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


#define o formulario da noticia
class Criarnoticia(CreateView):
    model = Noticia
    fields = ['titulo','texto']
    template_name = 'criar-noticia.html'
    success_url = '.'

def noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias.html', {'noticias': noticias})


def noticia(request, id=None):
    noticia = get_object_or_404(Noticia, id=id)
    return render(request, 'noticia.html', {'noticia': noticia})
