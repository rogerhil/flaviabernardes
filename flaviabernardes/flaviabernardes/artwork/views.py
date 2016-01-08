from django.views.generic import ListView

from ..utils import JsonView
from ..cms.models import Page
from .models import Artwork


class PaintingsView(ListView):
    context_object_name = 'artwork_list'
    queryset = Artwork.objects.filter(listing=True).order_by('-order')
    template_name = 'artwork/artworks.html'

    def get_context_data(self, **kwargs):
        context = super(PaintingsView, self).get_context_data(**kwargs)
        context['page'] = Page.objects.get(name='artworks')
        return context


class ArtworksSortJson(JsonView):

    def json_post(self, request, *args, **kwargs):
        ids = request.POST.getlist('data[]')
        for index, artwork_id in enumerate(ids):
            index += 1
            artwork = Artwork.objects.get(pk=artwork_id)
            artwork.order = index
            artwork.save()
