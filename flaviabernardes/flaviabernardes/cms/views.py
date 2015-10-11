from django.contrib.contenttypes.models import ContentType
from django.views.generic import DetailView

from ..utils import JsonView


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

    def get_queryset(self):
        app = self.kwargs['app']
        model = self.kwargs['draft_model']
        ct = ContentType.objects.get(app_label=app, model=model)
        return ct.model_class().objects.all()

    def get_context_data(self, **kwargs):
        context = super(CmsDraftPreview, self).get_context_data(**kwargs)
        obj = self.get_object()
        context['preview'] = True
        context[obj.cms.context_object_name] = obj
        if obj.cms.template_preview is 'PAGE':
            context['extend_template'] = self.page_preview_templates.get(
                                                                      obj.name)
        else:
            context['extend_template'] = obj.cms.template_preview
        return context
