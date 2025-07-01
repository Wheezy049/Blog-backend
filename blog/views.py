from django.shortcuts import render
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework import generics

# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all().order_by('-created_at')
    serializer_class = BlogPostSerializer

class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer