from mailchimp import Mailchimp

from django.conf import settings
from django import forms


class SubscriberForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=255, required=False)
    last_name = forms.CharField(max_length=255, required=False)

    def subscribe(self):
        data = self.cleaned_data
        client = Mailchimp(settings.MAILCHIMP_API_KEY)
        try:
            client.lists.unsubscribe(settings.MAILCHIMP_SUBSCRIBERS_LIST_ID,
                                     data)
        except:
            pass
        client.lists.subscribe(settings.MAILCHIMP_SUBSCRIBERS_LIST_ID, data)
