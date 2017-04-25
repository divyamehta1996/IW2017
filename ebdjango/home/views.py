# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from home.models import Facebook, Users
from .forms import Signup
from .forms import UserForm
from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required

def index(request):
	html = gethtml()
	return HttpResponse(html)

   # return HttpResponse('My first view.')
def login_notfb(request):
	username = request.POST.get('username')
	password=username = request.POST.get('password1')
	user = authenticate(request, username=username, password=password)
	if user is not None:
		print "Success!"
		login(request, user)
		return HttpResponseRedirect('http://localhost:8000/search')
	else:
		print "error"
		return render(request, 'login_notfb.html')


def gethtml():
	f =  open("home/index2.html", "r")
	r = f.read()
	return r

def privacypolicy(request):
	html = privacyhtml()
	return HttpResponse(html)

def privacyhtml():
	f = open("home/privacypolicy.html", "r")
	r = f.read()
	return r

def fblogin(request):
	f = open("home/loginfb.html", "r")
	r = f.read()
	return HttpResponse(r)

def results(request):
	a_list = Facebook.objects.all()
	context = {'results_list': a_list}
	return render(request, 'results.html', context)

	# f = open("home/results.html", "r")
	# r = f.read()
	# return HttpResponse(r)

def search(request):
	f = open("home/search.html", "r")
	r = f.read()
	return HttpResponse(r)

def specifics(request):
	f = open("home/price.html", "r")
	r = f.read()
	return HttpResponse(r)

def signup(request):
	# form = Signup(request.POST)
	# form1 = UserForm(request.POST)
	# if form.is_valid() and form1.is_valid():
	# 	print "hi"
	# 	new = form.save()
	# 	new1 = form1.save()
	# 	username = request.POST['username']
	# 	print username
	# 	password = request.POST['password']
	# 	print password
	# 	user = User.objects.create_user(username, password)
	# 	user.save()
	# 	login(request, user)
	# 		# redirect to a new URL:
	# 	return HttpResponseRedirect('http://localhost:8000/search')
	# return render(request, 'signup.html', {'form': form, 'form1': form1})



	if request.method == 'POST':
	 	form = Signup(request.POST)
	 	form1 = UserForm(request.POST)
	 # check whether it's valid:
	 	if form.is_valid() and form1.is_valid():
	 	# process the data in form.cleaned_data as required
	 		new = form.save()
	 		new1 = form1.save()
	 		user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
			user.save()
			login(request, user)
			return HttpResponseRedirect('http://localhost:8000/search')
	else:
		return render(request, 'signup.html')
	# 		user = authenticate(username=request.POST['username'], password=request.POST['password1'])
	# 		login(request, user)
	# 		# redirect to a new URL:
	# 		return HttpResponseRedirect('http://localhost:8000/search')
	# else: 
	# 	form = Signup(request.GET)
	# 	form1 = UserForm(request.GET)
	# return render(request, 'signup.html', {'form': form, 'form1': form1})

