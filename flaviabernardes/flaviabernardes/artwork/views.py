from django.views.generic import ListView
from django.template import RequestContext
from django.template.loader import get_template

from ..utils import JsonView
from ..cms.models import Page
from .models import Artwork, ArtworkType, Tag


class PaintingsView(ListView):
    context_object_name = 'artwork_list'
    queryset = Artwork.objects.filter(listing=True).order_by('-order')
    template_name = 'artwork/artworks.html'

    def get_context_data(self, **kwargs):
        context = super(PaintingsView, self).get_context_data(**kwargs)
        context['types'] = ArtworkType.objects.all()
        context['tags'] = Tag.objects.all()
        context['page'] = Page.objects.get(name='artworks')
        return context


class ArtworksSortJson(JsonView):

    def json_post(self, request, *args, **kwargs):
        ids = request.POST.getlist('data[]')
        index = len(ids)
        for artwork_id in ids:
            artwork = Artwork.objects.get(pk=artwork_id)
            artwork.order = index
            artwork.save()
            index -= 1
        print([a.order for a in Artwork.objects.filter(listing=True).order_by('-order')])


class ArtworksFilter(JsonView):

    def json_get(self, request, *args, **kwargs):
        tag_id = request.GET.get('tag')
        artworks = Artwork.objects.filter(listing=True, tags__id=tag_id)
        template = get_template('artwork/artworks_list.html')
        context = dict(artwork_list=artworks)
        rendered = template.render(RequestContext(request, context))
        return rendered
