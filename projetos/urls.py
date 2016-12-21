from django.conf.urls import url
from projetos import views
from projetos.views import IncluirProjeto


urlpatterns = [
    url(r'^$', views.projetos, name='projetos'),
    url(r'^(?P<id>[0-9]+)/$', views.projeto, name='projeto'),
    url(r'^incluir/$', IncluirProjeto.as_view(), name='incluir_projeto'),
    url(r'^(?P<id>[0-9]+)/excluir/$', views.excluir, name='excluir_projeto'),

]

