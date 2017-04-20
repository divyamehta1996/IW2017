from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	html = gethtml()
	return HttpResponse(html)

   # return HttpResponse('My first view.')

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
	f = open("home/results.html", "r")
	r = f.read()
	return HttpResponse(r)

def search(request):
	f = open("home/search.html", "r")
	r = f.read()
	return HttpResponse(r)

def specifics(request):
	f = open("home/price.html", "r")
	r = f.read()
	return HttpResponse(r)