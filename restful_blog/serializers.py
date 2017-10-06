from rest_framework import serializers

from django.contrib.auth.models import User

from restful_blog.models import Post

class PostSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Post
		fields = ('id', 'owner', 'title', 'created', 'timestamp', 'description', 'text')

class UserSerializer(serializers.ModelSerializer):
	posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

	class Meta:
		model = User
		fields = ('id', 'username', 'posts')