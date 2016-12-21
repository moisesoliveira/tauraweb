from django.conf.urls import url
from membros import views
from membros.views import CriaMembro, membro
from views import logar, sair
#from taura import urls

urlpatterns = [
    url(r'^$', views.membros, name='membros'),
    url(r'^(?P<id>[0-9]+)/$', views.membro, name='membro'),
    url(r'^(?P<id>[0-9]+)/excluir/$', views.excluir, name='excluir_membro'),
    url(r'^criar/$', CriaMembro.as_view(), name='criar_membro'),
##    url(r'^atualizar/(?P<pk>\d+)/$', AtualizarAutor.as_view(), name='atualizar_autor'),
    url(r'^login/$', logar, name='login'),
    url(r'^logout/$', sair, name='logout'),

]
