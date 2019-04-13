from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


class Register(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('home')
	template_name = 'registration/register.html'

	def form_valid(self, form):
		form.save()
		username = self.request.POST['username']
		password = self.request.POST['password1']
		user = authenticate(username=username, password=password)
		login(self.request, user)
		return HttpResponseRedirect(reverse('home'))
