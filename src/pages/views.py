from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
	print(request.user)
	context = { 

	}
	return render(request, "home.html", context)


def contacts_view(request, *args, **kwargs):
	return render(request, "contacts.html", {})


def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})
