from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	html = gethtml()
	return HttpResponse(html)

   # return HttpResponse('My first view.')

def gethtml():
	f =  open("home/index.html", "r")
	r = f.read()
	return r

def privacypolicy(request):
	html = privacyhtml()
	return HttpResponse(html)

def privacyhtml():
	f = open("home/privacypolicy.html", "r")
	r = f.read()
	return r