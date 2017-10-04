from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import restful_blog.views

urlpatterns = [
    url(r'^$', restful_blog.views.index, name='index'),
    url(r'^latest/', restful_blog.views.get_latest_post, name='latest'),
    url(r'^posts/', restful_blog.views.get_all_posts, name='all'),
    url(r'^admin/', include(admin.site.urls)),
]
