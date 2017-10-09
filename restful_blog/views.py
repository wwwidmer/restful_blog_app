from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework import generics

from restful_blog.models import Post
from restful_blog.permissions import IsOwnerOrReadOnly
from restful_blog.serializers import PostSerializer, UserSerializer


def index(request):
    return render(request, 'index.html')


@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
		'posts': reverse('post-list', request=request, format=format),
	})

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	'''
	CRUD operations for a single Post
	'''
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

class PostList(generics.ListCreateAPIView):
	'''
	List all Post Objects or create one
	'''
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
