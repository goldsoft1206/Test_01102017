from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

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
