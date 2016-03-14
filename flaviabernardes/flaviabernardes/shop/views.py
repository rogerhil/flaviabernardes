from django.shortcuts import render
from django.views.generic import ListView

from ..cms.models import Page
from .models import Original, Print


class ShopOriginalsView(ListView):
    context_object_name = 'shop_items'
    queryset = Original.objects.filter().order_by('-order')
    template_name = 'shop/shop.html'

    def get_context_data(self, **kwargs):
        context = super(ShopOriginalsView, self).get_context_data(**kwargs)
        context['page'] = Page.objects.get(name='shop/originals')
        return context


class ShopPrintsView(ListView):
    context_object_name = 'shop_items'
    queryset = Print.objects.filter().order_by('-order')
    template_name = 'shop/shop.html'

    def get_context_data(self, **kwargs):
        context = super(ShopPrintsView, self).get_context_data(**kwargs)
        context['page'] = Page.objects.get(name='shop/prints')
        return context
