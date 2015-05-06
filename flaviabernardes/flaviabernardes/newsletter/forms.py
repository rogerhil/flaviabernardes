from mailchimp import Mailchimp

from django.conf import settings
from django import forms

from .models import Subscriber, List, Subscription

BASE_URL = 'http://www.flaviabernardesart.com'


class SubscriberForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=255, required=False)
    last_name = forms.CharField(max_length=255, required=False)

    def subscribe(self):
        data = self.cleaned_data
        client = Mailchimp(settings.MAILCHIMP_API_KEY)
        list_id = settings.MAILCHIMP_SUBSCRIBERS_LIST_ID
        list_name = settings.MAILCHIMP_SUBSCRIBERS_LIST_NAME
        try:
            client.lists.unsubscribe(list_id, data)
        except:
            pass
        #if settings.DEVELOPMENT:
        #    return

        #subscriber = Subscriber.objects.get_or_create(**data)[0]
        #data['redirect'] = '%s/confirmation/?s=%s' % (BASE_URL,
        #                                              subscriber.uuid)
        client.lists.subscribe(list_id, data, data)
        #slist = List.objects.get_or_create(list_id=list_id, name=list_name)[0]
        #Subscription.objects.create(list=slist, subscriber=subscriber)
