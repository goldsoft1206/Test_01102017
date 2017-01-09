from django.conf.urls import url

from .views import UserListView, UserCreateView, UserUpdateView


urlpatterns = [
	url(r'^list/$', UserListView.as_view(), name='list'),
	url(r'^create/$', UserCreateView.as_view(), name='create'),
	url(r'^update/(?P<pk>\d+)/$', UserUpdateView.as_view(), name='update'),
]