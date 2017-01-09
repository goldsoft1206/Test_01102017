from django.conf.urls import url

from .views import UserListView, UserCreateView


urlpatterns = [
	url(r'^list/$', UserListView.as_view(), name='list'),
	url(r'^create/$', UserCreateView.as_view(), name='create'),
]