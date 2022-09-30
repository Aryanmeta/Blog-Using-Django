from django.views import generic
from django.urls import reverse_lazy

from .models import Post
from .form import NewPostForm


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
