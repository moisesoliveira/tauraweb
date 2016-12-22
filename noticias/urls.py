from django.conf.urls import url
from noticias import views
from noticias.views import Criarnoticia


urlpatterns = [
    url(r'^$', views.noticias, name='noticias/'),
    url(r'^(?P<id>[0-9]+)/$', views.noticia, name='noticia'),
    url(r'^criar/$', Criarnoticia.as_view(), name='criar_noticia'),

]