from mailchimp import Mailchimp, ListAlreadySubscribedError
from madmimi import MadMimi

import mailerlite

from django.conf import settings


class AlreadySubscribedError(Exception):

    def __init__(self, message, uuid, *args, **kwargs):
        super(Exception, self).__init__(message, *args, **kwargs)
        self.uuid = uuid


class EmailMarketing(object):

    def __init__(self):
        self._client = None

    @property
    def client(self):
        if self._client is None:
            if self.is_madmimi():
                self._client = MadMimi(settings.MADMIMI_USER,
                                       settings.MADMIMI_API_KEY)
            elif self.is_mailchimp():
                self._client = Mailchimp(settings.MAILCHIMP_API_KEY)
            elif self.is_mailerlite():
                self._client = mailerlite.Api(
                                           api_key=settings.MAILERLITE_API_KEY)
            else:
                raise NotImplementedError('EmailMarketing provider %s is '
                        'invalid.' % settings.CURRENT_EMAIL_MARKETING_PROVIDER)
        return self._client

    def is_madmimi(self):
        cur = settings.CURRENT_EMAIL_MARKETING_PROVIDER
        return cur == settings.MADMIMI

    def is_mailchimp(self):
        cur = settings.CURRENT_EMAIL_MARKETING_PROVIDER
        return cur == settings.MAILCHIMP

    def is_mailerlite(self):
        cur = settings.CURRENT_EMAIL_MARKETING_PROVIDER
        return cur == settings.MAILERLITE

    def create_list(self, list_id, name=None):
        if self.is_mailchimp():
            raise NotImplementedError("Mailchimp does not support create list "
                                      "at the moment")
        elif self.is_madmimi():
            return self.client.add_list(list_id)
        elif self.is_mailerlite():
            return self.client.create_list(name)
        else:
            raise NotImplementedError('EmailMarketing provider %s is '
                        'invalid.' % settings.CURRENT_EMAIL_MARKETING_PROVIDER)

    def subscribe(self, email, list_id, **kwargs):
        if self.is_mailchimp():
            try:
                self.client.lists.subscribe(list_id, dict(email=email), kwargs)
            except ListAlreadySubscribedError as err:
                raise AlreadySubscribedError(str(err))
        elif self.is_madmimi():
            contact = (kwargs.get('first_name'), kwargs.get('last_name'),
                       email, list_id)
            self.client.add_contacts([contact], audience_list=list_id)
            #self.client.subscribe(email, list_id)
        elif self.is_mailerlite():
            self.client.subscribe(
                list_id=list_id,
                email=email,
                fields=dict(last_name=kwargs.get('last_name'),
                            name=kwargs.get('first_name'))
            )
        else:
            raise NotImplementedError('EmailMarketing provider %s is '
                        'invalid.' % settings.CURRENT_EMAIL_MARKETING_PROVIDER)

    def unsubscribe(self, email, list_id):
        if self.is_mailchimp():
            self.client.lists.unsubscribe(list_id, dict(email=email))
        elif self.is_madmimi():
            self.client.unsubscribe(email, list_id)
        elif self.is_mailerlite():
            self.client.unsubscribe(email)
        else:
            raise NotImplementedError('EmailMarketing provider %s is '
                        'invalid.' % settings.CURRENT_EMAIL_MARKETING_PROVIDER)
