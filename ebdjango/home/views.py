# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from home.models import Users, UserWishlist
from .forms import Signup
from .forms import UserForm
from .forms import Wishlist
from .forms import Checklist
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget

#from django.contrib.auth.decorators import login_required

def index(request):
	return render(request, 'index2.html')

   # return HttpResponse('My first view.')
def login_notfb(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		print "post request"
		login(request, user)

		if request.user.is_authenticated():
			login(request, user)
			print "success!"
			return render(request, 'search.html')
		else:
			print"error"
			return render(request, 'login_notfb.html')
	else:
		print "that didnt work"
		return render(request, 'login_notfb.html')


	# username = request.POST.get('username')
	# password=username = request.POST.get('password1')
	# user = authenticate(request, username=username, password=password)
	# if user is not None:
	# 	print "Success!"
	# 	login(request, user)
	# 	return HttpResponseRedirect('http://localhost:8000/search')
	# else:
	# 	print "error"
	# 	return render(request, 'login_notfb.html')
def logoutuser(request):
	logout(request)
	return render(request, 'index2.html')

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
	if request.method == 'GET': # If the form is submitted
		search_query = request.GET.get('search_box', None)
		pref = request.GET.get('options')
		a_list = Users.objects.filter(name=search_query)
		print pref
		for a in a_list:
			print a
		if pref == 'obj':
			preference = 'object'
			context = {'results_list': a_list, 'pref': preference}
			print "success"
			return render(request, 'results.html', context)
		if pref == 'exp':
			preference = 'experience'
			context = {'results_list': a_list, 'pref': preference}
			print "success"
			return render(request, 'results.html', context)
	else:
		print "failure"
		render(request, 'search.html')
	# f = open("home/results.html", "r")
	# r = f.read()
	# return HttpResponse(r)

def search(request):
	if request.method == 'GET': # If the form is submitted
		search_query = request.GET.get('search_box', None)
		pref = request.GET.get('options')

		a_list = Users.objects.filter(name=search_query)
		#for a in a_list:
			#print a
		context = {'results_list': a_list, 'pref': pref}
		print "success"
		return render(request, 'search.html', context)
	




	else:
		print "failure"
		render(request, 'search.html')

def specifics(request):
	f = open("home/price.html", "r")
	r = f.read()
	return HttpResponse(r)

def signup(request):
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		
		form = Signup(request.POST)
		form_user = UserForm(request.POST)
		# check whether it's valid:
		if form.is_valid() and form_user.is_valid():
			# process the data in form.cleaned_data as required
			new_user = form_user.save()
			new_info = form.save(commit=False)
			new_info.user = new_user
			new_info.save()
			print "saved"
			user = authenticate(username=request.POST['username'], password=request.POST['password1'])
			if user.is_authenticated():
				print "succes"
				login(request, user)
			else:
				print "errorrrr"
			# redirect to a new URL:
			return HttpResponseRedirect('http://localhost:8000/search/')
		# if a GET (or any other method) we'll create a blank form
	else: 
		form = Signup()
		form_user = UserForm()
	return render(request, 'signup.html', {'form': form, 'form_user': form_user})

def wishlist(request):
	if request.method == 'POST':
		form = Wishlist(request.POST)
		item = request.POST['item']
		print item
		if form.is_valid():
			new = form.save(commit=False)
			print "hi"
			new.username = request.user
			print "hi2"
			print request.user
			new.save()
			print "valid"
		return HttpResponseRedirect('http://localhost:8000/wishlist/')
	else: 
		print "invalid"
		form = Wishlist()
	return render(request, 'wishlist.html', {'form': form})

def wishlistList(request, username=None):
	print username
	if username is not None:
		# get the name of the user 
		wisher = Users.objects.filter(username=username)
		# get their wishes
		if UserWishlist.objects.filter(username=username):
			print "wishes"
			a_list = UserWishlist.objects.filter(username=username)
			context = {'wish_list': a_list, 'wisher': wisher}
			return render(request, 'wishlistList.html', context)
	return render(request, 'wishlistList.html')

def faq(request):
	return render(request, 'faq.html')




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

	# 		user = authenticate(username=request.POST['username'], password=request.POST['password1'])
	# 		login(request, user)
	# 		# redirect to a new URL:
	# 		return HttpResponseRedirect('http://localhost:8000/search')
	# else: 
	# 	form = Signup(request.GET)
	# 	form1 = UserForm(request.GET)
	# return render(request, 'signup.html', {'form': form, 'form1': form1})

