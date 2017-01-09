from django.conf.urls import url

from .views import UserListView, UserCreateView, UserUpdateView, UserDetailView, UserDeleteView


urlpatterns = [
	url(r'^$', UserListView.as_view(), name='list'),
	url(r'^create/$', UserCreateView.as_view(), name='create'),
	url(r'^update/(?P<pk>\d+)/$', UserUpdateView.as_view(), name='update'),
	url(r'^detail/(?P<pk>\d+)/$', UserDetailView.as_view(), name='detail'),
	url(r'^delete/(?P<pk>\d+)/$', UserDeleteView.as_view(), name='delete'),
]