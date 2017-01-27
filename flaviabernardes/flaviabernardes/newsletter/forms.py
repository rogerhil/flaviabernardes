# -*- coding: <nome da codificação> -*-

from django.conf import settings
from django import forms
from django.core.mail import send_mail

from .client import EmailMarketing, AlreadySubscribedError
from .models import Subscriber, List, Subscription


BASE_URL = 'http://www.flaviabernardesart.com'


class BaseSubscriberForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255, required=False)
    list_id = forms.CharField(widget=forms.HiddenInput)
    provider = forms.CharField(widget=forms.HiddenInput)

    def pre_subscribe_locally(self):
        data = self.cleaned_data
        list_id = data.pop('list_id')
        provider = data.pop('provider')
        list_obj = List.objects.get(list_id=list_id, provider=provider)
        try:
            subscriber = Subscriber.objects.get(email=data['email'])
            if subscriber.subscription_set\
                         .filter(list__list_id=list_obj.list_id).count():
                raise AlreadySubscribedError('User %s is already subscribed.'
                                             % data['email'], subscriber.uuid)
        except Subscriber.DoesNotExist:
            subscriber = Subscriber.objects.get_or_create(**data)[0]
        return subscriber, list_obj

    def send_confirmation(self, subscriber, list_obj):
        data = self.cleaned_data
        email = data['email']
        if list_obj.confirmation_page:
            path = list_obj.confirmation_page.get_absolute_url()
        else:
            path = '/confirmation/'
        link = "%s%s?l=%s&s=%s" % (BASE_URL, path, list_obj.id,
                                   subscriber.uuid)
        body = list_obj.email_message % dict(name=str(subscriber),
                                             link=link)
        #print()
        #print(body)
        #print()
        send_mail(list_obj.email_subject, body, settings.DEFAULT_FROM_EMAIL,
                  [email], html_message=body)

    def subscribe(self, subscriber, list_obj):
        email = subscriber.email
        client = EmailMarketing()
        #try:
        #    client.unsubscribe(email, self.list_obj.list_id)
        #except:
        #    pass
        #if settings.DEVELOPMENT:
        #    return
        client.subscribe(email, list_obj.list_id,
                         first_name=subscriber.first_name,
                         last_name=subscriber.last_name)
        Subscription.objects.get_or_create(list=list_obj,
                                           subscriber=subscriber)
