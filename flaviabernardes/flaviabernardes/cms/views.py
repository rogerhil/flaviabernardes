import os
import re

from datetime import datetime
from collections import OrderedDict
from bs4 import BeautifulSoup
from cssutils import parseStyle

from django.contrib.contenttypes.models import ContentType
from django.views.generic import DetailView, TemplateView
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings

from ..utils import JsonView, JsonFormView
from ..artwork.views import PaintingsView
from ..blog.views import BlogView, PostView
from ..views import AboutView, ContactView
from ..blog.models import Draft, Post
from .models import Page, PageDraft
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
        return {'url': obj.instance.get_absolute_url()}


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

    def dispatch(self, request, *args, **kwargs):
        resp = super(CustomPageView, self).dispatch(request, *args, **kwargs)
        slug = kwargs['slug']
        page = Page.objects.get(name=slug)
        if page.sub_page_of:
            kwargs['subslug'] = kwargs['slug']
            kwargs['slug'] = page.sub_page_of.name
            return HttpResponseRedirect(reverse('sub_page', kwargs=kwargs))
        return resp

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
        j = lambda f: dict(path="/media/%s" % os.path.join(settings.UPLOAD_CMS_IMAGES_PATH, f['path']).split('media/')[-1], date=f['date'])
        date_format = lambda x : datetime.fromtimestamp(x).strftime('%b %d, %Y')
        files = [dict(path=os.path.join(settings.UPLOAD_CMS_IMAGES_PATH, f),
                      timestamp=os.path.getmtime(os.path.join(settings.UPLOAD_CMS_IMAGES_PATH, f)),
                      date=date_format(os.path.getmtime(os.path.join(settings.UPLOAD_CMS_IMAGES_PATH, f))))
                 for f in os.listdir(settings.UPLOAD_CMS_IMAGES_PATH)]
        sorted_files = reversed(sorted(files, key=lambda x: x['timestamp']))
        paths = OrderedDict()
        for item in sorted_files:
            paths.setdefault(item['date'], [])
            paths[item['date']].append(j(item))
        return {'paths': sorted(paths.items(), key=lambda x: x[1][0]['timestamp'])}


class PurgeUnusedImagesView(JsonView):

    bg_url_regex = re.compile(r'.*url\(["\']{0,1}([\w\-/]+)["\']{0,1}\).*')

    @classmethod
    def get_images(cls, items):
        imgs = set()
        attrs = ['content1', 'content2', 'content3', 'content4', 'text',
                 'text2', 'text3']
        a = lambda c: set([os.path.split(i.attrs['src'])[1] for i in
                           BeautifulSoup(c or "", "html.parser").find_all('img')])

        def b(c):
            bg_imgs = set()
            for i in BeautifulSoup(c or "", "html.parser").select('[style]'):
                style = parseStyle(i.attrs['style'])
                m = cls.bg_url_regex.match(style.background)
                if m:
                    bg_imgs |= os.path.split(m.groups()[0])[1]
                m = cls.bg_url_regex.match(style.backgroundImage)
                if m:
                    bg_imgs |= os.path.split(m.groups()[0])[1]
            return bg_imgs

        for item in items:
            for attr in attrs:
                value = getattr(item, attr, None)
                if value is not None:
                    imgs |= a(value)
                    imgs |= b(value)
        return imgs

    def get_unused_images(self):
        used = self.get_images(PageDraft.objects.all())
        used |= self.get_images(Page.objects.all())
        used |= self.get_images(Draft.objects.all())
        used |= self.get_images(Post.objects.all())
        current = os.listdir(settings.UPLOAD_CMS_IMAGES_PATH)
        return set(current) - used

    def json_get(self, request, *args, **kwargs):
        unused = list(self.get_unused_images())
        j = lambda f: "/media/%s" % os.path.join(
                       settings.UPLOAD_CMS_IMAGES_PATH, f).split('media/')[-1]
        paths = [j(f) for f in unused]
        return {'paths': paths}

    def json_post(self, request, *args, **kwargs):
        unused = list(self.get_unused_images())
        removed = []
        for img in unused:
            path = os.path.join(settings.UPLOAD_CMS_IMAGES_PATH, img)
            #os.remove(path)
            removed.append(path)
        return {'removed': removed}
