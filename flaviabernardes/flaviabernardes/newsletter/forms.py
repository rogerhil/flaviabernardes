# -*- coding: <nome da codificação> -*-

from django.conf import settings
from django import forms
from django.core.mail import send_mail

from .client import EmailMarketing, AlreadySubscribedError
from .models import Subscriber, List, Subscription


BASE_URL = 'http://www.flaviabernardesart.com'


class BaseSubscriberForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=255, required=False)
    last_name = forms.CharField(max_length=255, required=False)

    confirmation_url = '%s/confirmation/?s=%%s' % BASE_URL
    list_id = None
    subject = ""
    body = ""

    def pre_subscribe_locally(self):
        data = self.cleaned_data
        try:
            subscriber = Subscriber.objects.get(email=data['email'])
            if subscriber.subscription_set\
                         .filter(list__list_id=self.list_id).count():
                raise AlreadySubscribedError('User %s is already subscribed.'
                                             % data['email'])
        except Subscriber.DoesNotExist:
            subscriber = Subscriber.objects.get_or_create(**data)[0]
        return subscriber

    def send_confirmation(self, subscriber):
        email = self.cleaned_data['email']
        redirect = self.confirmation_url % subscriber.uuid
        body = self.body % (str(subscriber), redirect)
        send_mail(self.subject, body, settings.DEFAULT_FROM_EMAIL, [email])

    def subscribe(self, subscriber):
        email = subscriber.email
        client = EmailMarketing()
        #try:
        #    client.unsubscribe(email, self.list_id)
        #except:
        #    pass
        #if settings.DEVELOPMENT:
        #    return
        client.subscribe(email, self.list_id, first_name=subscriber.first_name,
                        last_name=subscriber.last_name)
        list_id, list_name = client.newsletter_id_name()
        slist = List.objects.get_or_create(list_id=list_id, name=list_name)[0]
        Subscription.objects.get_or_create(list=slist, subscriber=subscriber)


class SubscriberForm(BaseSubscriberForm):

    subject = "Confirm your subscription and download your artwork"
    body = "Hello %s, \n\n" \
        "Please follow the link below to download your free wallpaper " \
        "artwork. \n\n" \
        "If you can't click it, please copy the entire link and paste it " \
        "into your browser. \n\n" \
        "%s\n\n" \
        "Thank you,\n\n" \
        "Flavia Bernardes\n"

    list_id = settings.MADMIMI_NEWSLETTER_LIST_ID


class OauauSubscriberForm(BaseSubscriberForm):

    subject = "Confirme seu e-mail para baixar o livro de atividades do au au"
    body = "Olá %s, \n\n" \
        "Clique no link abaixo para fazer o download do livro de atividades " \
        "do au au.\n\n" \
        "Caso o link esteja inativo, copie e cole no seu browser.\n\n" \
        "%s\n\n" \
        "Obrigada,\n\n" \
        "Flavia Bernardes e o au au"

    confirmation_url = '%s/oauau/livro-de-atividades/?s=%%s' % BASE_URL

    list_id = settings.MADMIMI_OAUAU_LIST_ID
