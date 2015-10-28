from django.views.generic import ListView, TemplateView

from .cms.models import Page


class HomeView(TemplateView):
    context_object_name = 'home_artwork_list'
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['page'] = Page.objects.get(name='about')
        return context


class ContactView(TemplateView):
    template_name = 'contact/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['page'] = Page.objects.get(name='contact')
        return context
