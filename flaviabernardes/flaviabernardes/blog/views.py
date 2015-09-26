from django.views.generic import ListView, DetailView

from ..utils import JsonView
from .models import Post, Draft


class BlogView(ListView):

    context_object_name = 'posts_list'
    queryset = Post.objects.all().order_by('-created')
    template_name = 'blog/blog.html'


class PostView(DetailView):
    context_object_name = 'post'
    template_name = 'blog/post.html'
    model = Post


class DraftPublishView(JsonView, DetailView):
    model = Draft

    def json_post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.publish()
        return {}


class PostNewDraftView(JsonView, DetailView):
    model = Post

    def json_post(self, request, *args, **kwargs):
        obj = self.get_object()
        draft = obj.new_draft()
        return {'draft_id': draft.id}
