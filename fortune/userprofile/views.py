from django.shortcuts import render
from django.views.generic import ListView

from .models import UserProfile


class UserListView(ListView):
	"""
	View to list all users
	"""
	model = UserProfile
	template_name = "users/list.html"
