"""ebdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
# Add this import
from django.contrib.auth import views
#from home.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logout/', include('django.contrib.auth.urls')),
    url(r'^', include('home.urls')),
    url(r'^signup/', include('home.urls')),
    url(r'^login/', include('home.urls')),

    #url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name="login"),
    #url(r'^logout/$', views.logout, {'next_page': '/login'}),  
 
]
