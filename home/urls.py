from django.conf.urls import url
from views import home
from .import views


urlpatterns = [
    # url(r'^$', home, name='home'),

    url(r'^home$', views.home),

]

