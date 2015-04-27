from django.views.generic import ListView

from ..utils import JsonView, JsonFormView
from .models import Artwork
from .forms import SubscriberForm


class LandPageView(JsonFormView):
    template_name = 'landpage.html'
    form_template = 'landingpage_form.html'
    form_class = SubscriberForm
    success_url = '/'

    def form_valid(self, form):
        form.subscribe()
        return super(LandPageView, self).form_valid(form)


class ConfirmationView(ListView):
    context_object_name = 'home_artwork_list'
    queryset = Artwork.objects.filter(home=True)
    template_name = 'confirmation.html'


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
