from django.shortcuts import render
from django.views.generic import ListView

from ..cms.models import Page
from ..utils import JsonView
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


class ShopSortJson(JsonView):

    def json_post(self, request, *args, **kwargs):
        ids = request.POST.getlist('data[]')
        shop_type = request.POST.get('shop_type')
        index = len(ids)
        if shop_type == 'originals':
            klass = Original
        elif shop_type == 'prints':
            klass = Print
        else:
            raise Exception("Unknown shop type %s." % shop_type)

        for item_id in ids:
            item = klass.objects.get(pk=item_id)
            item.order = index
            item.save()
            index -= 1
