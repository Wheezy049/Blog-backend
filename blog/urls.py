from django.urls import path
from .views import BlogPostListCreate, BlogPostDetail, RegisterUser, LoginUser, CurrentUserView

urlpatterns = [
    path('blog', BlogPostListCreate.as_view(), name='blog_post_list_create'),
    path('blog/<int:pk>', BlogPostDetail.as_view(), name='blog_post_detail'),
    path('register', RegisterUser.as_view(), name='register_user'),
    path('login', LoginUser.as_view(), name='login_user'),
    path('me', CurrentUserView.as_view(), name='current_user'),
]