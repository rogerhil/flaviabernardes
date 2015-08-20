from django.views.generic import ListView, DetailView, CreateView

from ..utils import JsonView
from .models import Blog, Draft


class BlogsView(ListView):

    context_object_name = 'blogs_list'
    queryset = Blog.objects.all().order_by('-created')
    template_name = 'blog/blogs.html'


class BlogView(DetailView):
    context_object_name = 'blog'
    template_name = 'blog/blog.html'
    model = Blog


class DraftPublishView(JsonView, DetailView):
    model = Draft

    def json_post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.publish()
        return {}


class BlogFormView(CreateView):
    context_object_name = 'blog'
    template_name = 'blog/blog_form.html'
    model = Blog


class BlogFieldForm(JsonView, DetailView):
    context_object_name = 'blog'
    template_name = 'blog/blog.html'
    model = Blog

    def json_post(self, request, *args, **kwargs):
        obj = self.get_object()
        for key, value in request.POST.items():
            setattr(obj, key, value)
        obj.save()

