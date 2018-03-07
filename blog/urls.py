from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),   
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^event/list/$', views.event_list, name='event_list'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^login/$', views.login, name='login'),
	url(r'^home/$', views.home, name='home'),
	url(r'^explore/$', views.explore, name='explore'),
	url(r'^profile_user/(?P<username>[a-zA-Z0-9]+)$', views.profile_user, name='profile_user'),
	#PicApril
	url(r'^upload_pic/$', views.upload_pic, name='upload_pic'),
]
