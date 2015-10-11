from django.views.generic import ListView, TemplateView

from .artwork.models import Artwork
from .cms.models import Page


class HomeView(ListView):
    context_object_name = 'home_artwork_list'
    queryset = Artwork.objects.filter(home=True)
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
