# -*- coding: <nome da codificação> -*-

from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

from ..utils import JsonFormView
from ..cms.models import Page
from .client import AlreadySubscribedError
from .forms import BaseSubscriberForm
from .models import Subscriber, List


class NewsletterBaseView(JsonFormView):

    already_msg = "You have already entered your name and email."

    def form_valid(self, form):
        try:
            subscriber, list_obj = form.pre_subscribe_locally()
            form.send_confirmation(subscriber, list_obj)
        except AlreadySubscribedError as err:
            form.errors['__all__'] = self.already_msg
            return self.form_invalid(form, extra_data={'s': err.uuid})
        return super(NewsletterBaseView, self).form_valid(form)


class NewsletterConfirmationBaseView(TemplateView):
    template_name = 'confirmation.html'
    redirect_name = 'home'
    subscription_form_class = BaseSubscriberForm

    def dispatch(self, request, *args, **kwargs):
        subscriber_uuid = request.GET.get('s')
        list_id = request.GET.get('l')
        if not list_id:
            return HttpResponseRedirect(reverse(self.redirect_name))
        list_obj = List.objects.get(pk=list_id)
        if not subscriber_uuid:
            return HttpResponseRedirect(reverse(self.redirect_name))
        try:
            subscriber = Subscriber.objects.get(uuid=subscriber_uuid)
        except Subscriber.DoesNotExist:
            return HttpResponseRedirect(reverse(self.redirect_name))
        form = self.subscription_form_class()
        form.subscribe(subscriber, list_obj)
        return super(NewsletterConfirmationBaseView, self).dispatch(request,
                                                               *args, **kwargs)


class LandPageView(NewsletterBaseView):
    template_name = 'landpage.html'
    form_template = 'landingpage_form.html'
    form_class = BaseSubscriberForm
    success_url = '/'
    redirect_name = 'landpage'


class ConfirmationView(NewsletterConfirmationBaseView):
    template_name = 'confirmation.html'
    subscription_form_class = BaseSubscriberForm


class CustomConfirmationView(NewsletterConfirmationBaseView):
    template_name = 'cms/generic_page_view.html'

    def get_context_data(self, **kwargs):
        context = super(CustomConfirmationView, self)\
                                                    .get_context_data(**kwargs)
        slug = kwargs['slug']
        try:
            context['page'] = Page.objects.get(name=slug)
        except Page.DoesNotExist:
            raise Http404()
        return context


class NewsletterView(NewsletterBaseView):
    form_class = BaseSubscriberForm
    template_name = 'newsletter/line_form.html'
    form_template = 'newsletter/line_form.html'
