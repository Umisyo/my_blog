from rest_framework import serializers
from .models import User, Blog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('blog_title', 'blog_text', 'created_at', 'updated_at', 'status')

