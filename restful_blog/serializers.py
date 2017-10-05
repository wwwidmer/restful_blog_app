from rest_framework import serializers
from restful_blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'created', 'timestamp', 'description', 'text')