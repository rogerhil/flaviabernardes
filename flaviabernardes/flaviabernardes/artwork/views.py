from django.views.generic import ListView
from django.template import RequestContext
from django.template.loader import get_template

from ..utils import JsonView
from ..cms.models import Page
from .models import Artwork, ArtworkType, Tag, TagArtwork


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
        tag_slug = request.POST.get('tag_slug')
        index = len(ids)
        for artwork_id in ids:
            tag_artwork = TagArtwork.objects.get(artwork__id=artwork_id,
                                                 tag__slug=tag_slug)
            tag_artwork.order = index
            tag_artwork.save()
            index -= 1


class ArtworksFilter(JsonView):

    def json_get(self, request, *args, **kwargs):
        slug = request.GET.get('slug')
        artworks = Artwork.objects.filter(listing=True, tags__slug=slug)\
                                  .order_by('link_to_tag')
        template = get_template('artwork/artworks_list.html')
        context = dict(artwork_list=artworks)
        rendered = template.render(RequestContext(request, context))
        return rendered
