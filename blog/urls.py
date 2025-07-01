from django.urls import path
from .views import BlogPostListCreate, BlogPostDetail

urlpatterns = [
    path('blog', BlogPostListCreate.as_view(), name='blog_post_list_create'),
    path('blog/<int:pk>', BlogPostDetail.as_view(), name='blog_post_detail'),
]