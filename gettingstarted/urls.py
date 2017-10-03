from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import restful_blog.views

urlpatterns = [
    url(r'^$', restful_blog.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
]
