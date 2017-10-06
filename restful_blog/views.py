from django.http import Http404
from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics

from restful_blog.models import Post
from restful_blog.serializers import PostSerializer


def index(request):
    return render(request, 'index.html')


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	'''
	CRUD operations for a single Post
	'''
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostList(generics.ListCreateAPIView):
	'''
	List all Post Objects or create one
	'''
	queryset = Post.objects.all()
	serializer_class = PostSerializer
