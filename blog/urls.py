from django.urls import path
from .views import PostListView, PostDetailView, CreatePostView, UpdatePostView, DeletePostView,   PostListApiView,UpdatePostApiView,CreatePostApiView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('<int:pk>/update/', UpdatePostView.as_view(), name='post_update'),
    path('<int:pk>/delete/', DeletePostView.as_view(), name='post_delete'),

    #api urls
    path('api/',PostListApiView.as_view(),name='list_api'),
    path('api/create/', CreatePostApiView.as_view()),
    path('api/<int:pk>/', UpdatePostApiView.as_view(),name='cred'),
]
