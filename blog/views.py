from django.views import generic
from django.urls import reverse_lazy

from .models import Post
from .form import NewPostForm

from .serializers import PostSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class PostListView(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datatime_modified')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post_detail'


class CreatePostView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/create_post.html'


class UpdatePostView(generic.UpdateView):
    form_class = NewPostForm
    template_name = 'blog/create_post.html'
    model = Post


class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')


#apis

class PostListApiView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class  = PostSerializer

class UpdatePostApiView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class CreatePostApiView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
