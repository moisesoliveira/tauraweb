"""taura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from django.contrib.auth import views
from membros.views import logar, sair
#from noticias.views import Criarnoticia
from django.views.generic.base import TemplateView




urlpatterns = [
    # Pagina inicial usando TemplateView (chama o HTML diretamente sem precisar de funcao ou classe na views.py)
#   url(r'^$', TemplateView.as_view(template_name="index.html")),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^CriaUsuario/', include('membros.urls')),
    url(r'^membros/', include('membros.urls')),
    url(r'^noticias/', include('noticias.urls')),
    url(r'^projetos/', include('projetos.urls')),
    url(r'^login/$', logar, name='login'),
    url(r'^logout/$', sair, name='logout'),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name = 'index'),
]