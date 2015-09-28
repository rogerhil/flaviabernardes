from django.views.generic import ListView, DetailView

from ..utils import JsonView
from .models import Post, Draft
from ..newsletter.forms import SubscriberForm


class BlogView(ListView):
    context_object_name = 'posts_list'
    queryset = Post.objects.all().order_by('-created')
    template_name = 'blog/blog.html'


class PostView(DetailView):
    context_object_name = 'post'
    template_name = 'blog/post.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['form'] = SubscriberForm()
        return context


class DraftPublishView(JsonView, DetailView):
    model = Draft

    def json_post(self, request, *args, **kwargs):
        obj = self.get_object()
        publish_old = bool(request.POST.get('publish_old', False))
        try:
            obj.publish(publish_old)
        except Draft.TooOldToPublish as err:
            return {'too_old': str(err)}
        return {}


class PostNewDraftView(JsonView, DetailView):
    model = Post

    def json_post(self, request, *args, **kwargs):
        obj = self.get_object()
        draft = obj.new_draft()
        return {'draft_id': draft.id}


class DraftPreview(DetailView):
    context_object_name = 'post'
    template_name = 'blog/post_preview.html'
    model = Draft

    def get_context_data(self, **kwargs):
        context = super(DraftPreview, self).get_context_data(**kwargs)
        context['post_preview'] = True
        return context
