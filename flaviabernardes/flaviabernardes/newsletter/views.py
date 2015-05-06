from mailchimp import ListAlreadySubscribedError

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView

from ..utils import JsonFormView
from .forms import SubscriberForm
from .models import Subscriber


class LandPageView(JsonFormView):
    template_name = 'landpage.html'
    form_template = 'landingpage_form.html'
    form_class = SubscriberForm
    success_url = '/'

    def form_valid(self, form):
        try:
            form.subscribe()
        except ListAlreadySubscribedError:
            msg = "You are already subscribed to my newsletter."
            form.errors['__all__'] = msg
            return self.form_invalid(form)
        return super(LandPageView, self).form_valid(form)


class ConfirmationView(ListView):
    context_object_name = 'home_artwork_list'
    template_name = 'confirmation.html'

    def dispatch(self, request, *args, **kwargs):
        subscriber_uuid = request.GET.get('s')
        #if not subscriber_uuid:
        #    return HttpResponseRedirect(reverse('landpage'))
        #try:
        #    Subscriber.objects.get(uuid=subscriber_uuid)
        #except Subscriber.DoesNotExist:
        #    return HttpResponseRedirect(reverse('landpage'))
        return super(ConfirmationView, self).dispatch(request, *args, **kwargs)
