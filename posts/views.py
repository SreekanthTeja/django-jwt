from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics
# Create your views here.
class PostListView(generics.ListAPIView):
    # permission_classes = (IsAuthenticated, )
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class RUDPostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer