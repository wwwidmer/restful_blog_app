from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from restful_blog import views

urlpatterns = [
    url(r'^$', views.PostList.as_view()),
	url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post-list'),
	url(r'^users/$', views.UserList.as_view(), name='user-list'),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
