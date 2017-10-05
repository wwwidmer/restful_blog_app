from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from restful_blog.models import Post
from restful_blog.serializers import PostSerializer

def index(request):
    return render(request, 'index.html')


@csrf_exempt
def post_detail(request, pk):
	'''
	CRUD operations for a single Post
	'''
	try:
		post = Post.objects.get(pk=pk)
	except Post.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = PostSerializer(post)
		return JsonResponse(serializer.data)
	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = PostSerializer(post, data=data)

		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)
	elif request.method == 'DELETE':
		post.delete()
		return HttpResponse(status=204)
	return response


@csrf_exempt
def post_list(request):
	'''
	List all Post objects or creates a new one.
	'''
	if request.method == 'GET':
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return JsonResponse(serializer.data, safe=False)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = PostSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)

	return JsonResponse(serializer.errors, status=400)