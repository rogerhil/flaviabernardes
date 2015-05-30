from django.conf import settings
from django import forms
from django.core.mail import send_mail

from .client import EmailMarketing
from .models import Subscriber, List, Subscription


BASE_URL = 'http://www.flaviabernardesart.com'

SUBJECT = "Click to confirm your subscription"
BODY = "To activate your subscription, please follow the link below. \n" \
       "If you can't click it, please copy the entire link and paste it " \
       "into your browser. \n\n%s"
FROM_EMAIL = "flavia@flaviabernardesart.com"


class SubscriberForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=255, required=False)
    last_name = forms.CharField(max_length=255, required=False)

    def pre_subscribe_locally(self):
        data = self.cleaned_data
        return Subscriber.objects.get_or_create(**data)[0]

    def send_confirmation(self, subscriber):
        email = self.cleaned_data['email']
        redirect = '%s/confirmation/?s=%s' % (BASE_URL, subscriber.uuid)
        body = BODY % redirect
        send_mail(SUBJECT, body, settings.DEFAULT_FROM_EMAIL, [email])

    def subscribe(self, subscriber):
        email = subscriber.email
        client = EmailMarketing()
        #try:
        #    client.unsubscribe_to_newsletter(email)
        #except:
        #    pass
        #if settings.DEVELOPMENT:
        #    return
        client.subscribe_to_newsletter(email, first_name=subscriber.first_name,
                                       last_name=subscriber.last_name)
        list_id, list_name = client.newsletter_id_name()
        slist = List.objects.get_or_create(list_id=list_id, name=list_name)[0]
        Subscription.objects.create(list=slist, subscriber=subscriber)
