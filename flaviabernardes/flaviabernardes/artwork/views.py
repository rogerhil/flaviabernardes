from django.views.generic import ListView
from .models import Artwork


class HomeView(ListView):

    context_object_name = 'home_artwork_list'
    queryset = Artwork.objects.filter(home=True)
    template_name = 'index.html'


class PaintingsView(ListView):

    context_object_name = 'artwork_list'
    queryset = Artwork.objects.all()
    template_name = 'artwork/artworks.html'
