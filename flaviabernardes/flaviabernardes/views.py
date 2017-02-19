import shopify

from django.conf import settings
from django.views.generic import ListView, TemplateView

from .cms.models import Page
from .utils import JsonView

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


class ShopifyProduct(JsonView):

    def json_get(self, request, *args, **kwargs):
        shop_url = "https://%s:%s@flavia-bernardes.myshopify.com/admin" % (
            settings.SHOPIFY_API_KEY, settings.SHOPIFY_PASSWORD)
        shopify.ShopifyResource.set_site(shop_url)
        shopify.Session.setup(api_key=settings.SHOPIFY_API_KEY,
                              secret=settings.SHOPIFY_SHARED_SECRET)
        product = shopify.Product.find(request.GET['pid'])
        return product.to_dict()
