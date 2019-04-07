from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
	print(request.user)
	#return HttpResponse("<h1>Home view</h1>")
	return render(request, "home.html", {})


def contacts_view(request, *args, **kwargs):
	return render(request, "contacts.html", {})


def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})
