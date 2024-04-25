from django.urls import path, include
from myapp.views import PostList, PostDetail

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
]
