from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

from ..utils import JsonFormView
from .client import AlreadySubscribedError
from .forms import SubscriberForm, OauauSubscriberForm
from .models import Subscriber


class NewsletterBaseView(JsonFormView):

    already_msg = "You are already subscribed to my newsletter."

    def form_valid(self, form):
        try:
            subscriber = form.pre_subscribe_locally()
            form.send_confirmation(subscriber)
        except AlreadySubscribedError:
            form.errors['__all__'] = self.already_msg
            return self.form_invalid(form)
        return super(NewsletterBaseView, self).form_valid(form)


class NewsletterConfirmationBaseView(TemplateView):
    template_name = 'confirmation.html'
    redirect_name = None

    def dispatch(self, request, *args, **kwargs):
        subscriber_uuid = request.GET.get('s')
        if not subscriber_uuid:
            return HttpResponseRedirect(reverse(self.redirect_name))
        try:
            subscriber = Subscriber.objects.get(uuid=subscriber_uuid)
        except Subscriber.DoesNotExist:
            return HttpResponseRedirect(reverse(self.redirect_name))
        form = SubscriberForm()
        form.subscribe(subscriber)
        return super(NewsletterConfirmationBaseView, self).dispatch(request,
                                                               *args, **kwargs)


class LandPageView(NewsletterBaseView):
    template_name = 'landpage.html'
    form_template = 'landingpage_form.html'
    form_class = SubscriberForm
    success_url = '/'
    redirect_name = 'landpage'


class ConfirmationView(NewsletterConfirmationBaseView):
    template_name = 'confirmation.html'


class OauauView(NewsletterBaseView):
    template_name = 'auau.html'
    form_template = 'landingpage_form.html'
    form_class = OauauSubscriberForm
    success_url = '/'
    already_msg = "Voce ja esta cadastado(a)"


class OauauConfirmationView(NewsletterConfirmationBaseView):
    template_name = 'confirmation.html'
    redirect_name = 'oauau'