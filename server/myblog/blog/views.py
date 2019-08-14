import django_filters
from rest_framework import viewsets, filters

from .models import User, Blog
from .serializer import UserSerializer, BlogSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializerclass = UserSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializerclass = BlogSerializer

