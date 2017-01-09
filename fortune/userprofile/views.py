import random

from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from .models import UserProfile
from .forms import UserForm


class UserListView(ListView):
	"""
	View to list all users
	"""
	model = UserProfile
	template_name = "users/list.html"


class UserCreateView(CreateView):
	"""
	View to create a user
	We define a custom form with username and birthdate field
	"""
	model = UserProfile
	form_class = UserForm
	template_name = 'users/create.html'

	def get_success_url(self):
		return reverse_lazy('users:list')

	def form_valid(self, form):
		# create user object first
		username = form.cleaned_data['username']
		user = User.objects.create_user(username)

		# generate random variable
		rand_val = random.randint(1, 100)

		# generate user profile
		profile = UserProfile(user=user, birth_date=form.cleaned_data['birth_date'], random_number=rand_val)
		profile.save()

		return HttpResponseRedirect(self.get_success_url())
