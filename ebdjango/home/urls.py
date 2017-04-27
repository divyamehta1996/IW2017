from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
#from home.forms import LoginForm

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^privacypolicy$', views.privacypolicy, name='privacypolicy'),
    url(r'^loginfb/', views.fblogin, name='fblogin'),
    url(r'^results/', views.results, name='results'),
    url(r'^search/', views.search, name='search'),
    url(r'^specifics/', views.specifics, name='specifics'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', views.login_notfb, name='login_notfb'),
    url(r'^wishlist/', views.wishlist, name='wishlist')
    #url(r'^login/', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
    #url(r'^logout/$', views.logout, {'next_page': '/login'}) 

]