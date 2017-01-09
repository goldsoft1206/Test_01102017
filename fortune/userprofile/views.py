import random

from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
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


class UserUpdateView(UpdateView):
	"""
	View to modify a user
	"""
	model = UserProfile
	form_class = UserForm
	template_name = 'users/update.html'

	def get_success_url(self):
		return reverse_lazy('users:list')

	def form_valid(self, form):
		# update username
		self.object.user.username = form.cleaned_data['username']
		# update birth_date
		self.object.birth_date = form.cleaned_data['birth_date']
		self.object.user.save()
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())

	def get_initial(self):
		init_value = super(UserUpdateView, self).get_initial()
		init_value['username'] = self.object.user.username
		return init_value


class UserDetailView(DetailView):
	"""
	View to show detailed info of User
	"""
	model = UserProfile
	template_name = 'users/detail.html'


class UserDeleteView(DeleteView):
	"""
	View to delete user
	"""
	model = UserProfile
	template_name = 'users/delete.html'
	success_url = reverse_lazy('users:list')

