from django.conf.urls import include, url
from django.contrib.auth.models import User
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers, serializers, viewsets

import restful_blog.views

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'is_staff')

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all();
	serializer_class =UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^rest-api-test/', include(router.urls)),
    url(r'^$', restful_blog.views.index, name='index'),
    url(r'^api/', include('restful_blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]


urlpatterns += [
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]