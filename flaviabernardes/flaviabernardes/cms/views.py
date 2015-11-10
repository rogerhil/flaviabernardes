import os
from datetime import datetime

from django.contrib.contenttypes.models import ContentType
from django.views.generic import DetailView, TemplateView
from django.http import Http404
from django.conf import settings

from ..utils import JsonView, JsonFormView
from ..artwork.views import PaintingsView
from ..blog.views import BlogView, PostView
from ..views import AboutView, ContactView
from ..blog.models import Draft
from .models import Page
from .forms import UploadFileForm


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
            template_name = self.page_preview_templates.get(obj.name)
            if template_name is None:
                template_name = 'cms/generic_page_view.html'
            context['extend_template'] = template_name
        else:
            if isinstance(obj, Draft):
                context.update(self.get_original_context('post', obj))
            context[obj.cms.context_object_name] = obj
            context['extend_template'] = obj.cms.template_preview
        return context


class SubPageView(TemplateView):
    template_name = 'cms/generic_page_view.html'

    def get_context_data(self, **kwargs):
        context = super(SubPageView, self).get_context_data(**kwargs)
        subslug = kwargs['subslug']
        try:
            context['page'] = Page.objects.get(name=subslug)
        except Page.DoesNotExist:
            raise Http404()
        return context


class CustomPageView(TemplateView):
    template_name = 'cms/generic_page_view.html'

    def get_context_data(self, **kwargs):
        context = super(CustomPageView, self).get_context_data(**kwargs)
        slug = kwargs['slug']
        try:
            page = Page.objects.get(name=slug)
            if page.is_newsletter_confirmation_page:
                raise Http404()
            context['page'] = page
        except Page.DoesNotExist:
            raise Http404()
        return context


class UploadImageView(JsonFormView):

    form_class = UploadFileForm

    def form_valid(self, form):
        if not os.path.isdir(settings.UPLOAD_CMS_IMAGES_PATH):
            os.makedirs(settings.UPLOAD_CMS_IMAGES_PATH)
        data = form.cleaned_data
        name = data['file'].name
        path = os.path.join(settings.UPLOAD_CMS_IMAGES_PATH, name)
        if os.path.isfile(path):
            name, ext = os.path.splitext(name)
            sufix = datetime.now().isoformat()
            name = "%s-%s%s" % (name, sufix, ext)
            path = os.path.join(settings.UPLOAD_CMS_IMAGES_PATH, name)
        with open(path, 'wb+') as afile:
            for chunk in data['file'].chunks():
                afile.write(chunk)
        return super(UploadImageView, self).form_valid(form)


class ImagesPathsView(JsonView):

    def json_get(self, request, *args, **kwargs):
        if not os.path.isdir(settings.UPLOAD_CMS_IMAGES_PATH):
            os.makedirs(settings.UPLOAD_CMS_IMAGES_PATH)
        j = lambda f: "/media/%s" % os.path.join(
                       settings.UPLOAD_CMS_IMAGES_PATH, f).split('/media/')[-1]
        paths = [j(f) for f in os.listdir(settings.UPLOAD_CMS_IMAGES_PATH)]
        return {'paths': paths}
