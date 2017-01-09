from django.conf.urls import url

from .views import UserListView


urlpatterns = [
	url(r'^list/$', UserListView.as_view(), name='list'),
]