from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^privacypolicy$', views.privacypolicy, name='privacypolicy'),
    url(r'^login$', views.fblogin, name='fblogin'),
    url(r'^results$', views.results, name='results'),
    url(r'^search$', views.search, name='search'),
    url(r'^specifics$', views.specifics, name='specifics')
]