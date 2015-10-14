from django.contrib.contenttypes.models import ContentType
from django.views.generic import DetailView

from ..utils import JsonView
from ..artwork.views import PaintingsView
from ..blog.views import BlogView, PostView
from ..views import AboutView, ContactView
from ..blog.models import Draft


class CmsDraftPublishView(JsonView, DetailView):

    def get_queryset(self):
        app = self.kwargs['app']
        model = self.kwargs['draft_model']
        ct = ContentType.objects.get(app_label=app, model=model)
        return ct.model_class().objects.all()

    def json_post(self, request, *args, **kwargs):
        obj = self.get_object()
        publish_old = bool(request.POST.get('publish_old', False))
        try:
            obj.publish(publish_old)
        except obj.TooOldToPublish as err:
            return {'too_old': str(err)}
        return {}


class CmsObjectNewDraftView(JsonView, DetailView):

    def get_queryset(self):
        app = self.kwargs['app']
        model = self.kwargs['model']
        ct = ContentType.objects.get(app_label=app, model=model)
        return ct.model_class().objects.all()

    def json_post(self, request, *args, **kwargs):
        obj = self.get_object()
        draft = obj.new_draft()
        return {'draft_id': draft.id}


class CmsDraftPreview(DetailView):
    context_object_name = 'draft'
    template_name = 'cms/preview.html'

    page_preview_templates = dict(
        artworks='artwork/artworks.html',
        blog='blog/blog.html',
        about='about/about.html',
        contact='contact/contact.html',
    )

    def get_original_context(self, name, obj=None):
        if name == 'artworks':
            pv = PaintingsView()
            pv.object_list = pv.get_queryset()
            return pv.get_context_data()
        elif name == 'blog':
            bv = BlogView()
            bv.object_list = bv.get_queryset()
            return bv.get_context_data()
        elif name == 'post':
            pv = PostView()
            pv.object = obj
            return pv.get_context_data()
        elif name == 'about':
            return AboutView().get_context_data()
        elif name == 'contact':
            return ContactView().get_context_data()
        else:
            return {}

    def get_queryset(self):
        app = self.kwargs['app']
        model = self.kwargs['draft_model']
        ct = ContentType.objects.get(app_label=app, model=model)
        return ct.model_class().objects.all()

    def get_context_data(self, **kwargs):
        context = super(CmsDraftPreview, self).get_context_data(**kwargs)
        obj = self.get_object()
        context['preview'] = True
        if obj.cms.template_preview is 'PAGE':
            context.update(self.get_original_context(obj.name))
            context[obj.cms.context_object_name] = obj
            context['extend_template'] = self.page_preview_templates.get(
                                                                      obj.name)
        else:
            if isinstance(obj, Draft):
                context.update(self.get_original_context('post', obj))
            context[obj.cms.context_object_name] = obj
            context['extend_template'] = obj.cms.template_preview
        return context
