from django.urls import path
from .views import PostListView, PostDetailView, CreatePostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('<int:pk>/update/', UpdatePostView.as_view(), name='post_update'),
    path('<int:pk>/delete/', DeletePostView.as_view(), name='post_delete'),
]
