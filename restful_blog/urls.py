from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from restful_blog import views

urlpatterns = [
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^$', views.post_list)
]

urlpatterns = format_suffix_patterns(urlpatterns)