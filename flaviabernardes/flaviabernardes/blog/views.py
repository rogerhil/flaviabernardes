from django.views.generic import ListView, DetailView

from .models import Post, Draft
from ..newsletter.forms import SubscriberForm
from ..cms.models import Page


class BlogView(ListView):
    context_object_name = 'posts_list'
    queryset = Post.objects.all().order_by('-created')
    template_name = 'blog/blog.html'

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['page'] = Page.objects.get(name='blog')
        return context


class PostView(DetailView):
    context_object_name = 'post'
    template_name = 'blog/post.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['form'] = SubscriberForm()
        return context
