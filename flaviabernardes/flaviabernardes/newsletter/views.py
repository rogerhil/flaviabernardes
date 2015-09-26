from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

from ..utils import JsonFormView
from .client import AlreadySubscribedError
from .forms import SubscriberForm
from .models import Subscriber

class BaseNewsletterView(JsonFormView):
    form_class = SubscriberForm
    success_url = '/'

    def form_valid(self, form):
        try:
            subscriber = form.pre_subscribe_locally()
            form.send_confirmation(subscriber)
        except AlreadySubscribedError:
            msg = "You are already subscribed to my newsletter."
            form.errors['__all__'] = msg
            return self.form_invalid(form)
        return super(BaseNewsletterView, self).form_valid(form)


class LandPageView(BaseNewsletterView):
    template_name = 'landpage.html'
    form_template = 'landingpage_form.html'


class ConfirmationView(TemplateView):
    template_name = 'confirmation.html'

    def dispatch(self, request, *args, **kwargs):
        subscriber_uuid = request.GET.get('s')
        if not subscriber_uuid:
            return HttpResponseRedirect(reverse('landpage'))
        try:
            subscriber = Subscriber.objects.get(uuid=subscriber_uuid)
        except Subscriber.DoesNotExist:
            return HttpResponseRedirect(reverse('landpage'))
        form = SubscriberForm()
        form.subscribe(subscriber)
        return super(ConfirmationView, self).dispatch(request, *args, **kwargs)


class NewsletterView(BaseNewsletterView):
    template_name = 'newsletter/line_form.html'
    form_template = 'newsletter/line_form.html'
