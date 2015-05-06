from django.views.generic import ListView

from ..utils import JsonView
from .models import Artwork


class HomeView(ListView):
    context_object_name = 'home_artwork_list'
    queryset = Artwork.objects.filter(home=True)
    template_name = 'index.html'


class PaintingsView(ListView):
    context_object_name = 'artwork_list'
    queryset = Artwork.objects.filter(listing=True).order_by('order')
    template_name = 'artwork/artworks.html'


class ArtworksSortJson(JsonView):

    def json_post(self, request, *args, **kwargs):
        ids = request.POST.getlist('data[]')
        for index, artwork_id in enumerate(ids):
            index += 1
            artwork = Artwork.objects.get(pk=artwork_id)
            artwork.order = index
            artwork.save()
