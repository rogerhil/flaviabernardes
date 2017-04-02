import uuid

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


from ..cms.models import Page
from .client import EmailMarketing

SIGN_UP_TITLE = "Want an exclusive artwork wallpaper? Sign up below"
DEFAULT_SUBJECT = "Confirm your subscription"
DEFAULT_MESSAGE = """<p>Hello %(name)s,</p>
<p>Please follow the link below.</p>
<p>If you can't click it, please copy the entire link and paste it into your
browser.</p>
<p>%(link)s</p>
<p>Thank you,</p>
<p>Flavia Bernardes</p>
"""


class Subscriber(models.Model):
    uuid = models.CharField(max_length=100, blank=True, unique=True,
                            default=uuid.uuid4)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    registered = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.full_name or self.email.split('@')[0]

    @property
    def full_name(self):
        return ("%s %s" % (self.first_name, self.last_name)).strip()


class List(models.Model):
    provider = models.CharField(max_length=32, editable=False,
                                default='mailerlite')
    list_id = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128)
    sign_up_title = models.CharField(max_length=255, default=SIGN_UP_TITLE,
                                     null=True, blank=True)
    confirmation_page = models.ForeignKey(Page,
                                  related_name='confirmation_newsletter_lists')
    email_subject = models.CharField(max_length=255, default=DEFAULT_SUBJECT)
    email_message = models.TextField(default=DEFAULT_MESSAGE)

    def __str__(self):
        return "%s (%s)" % (self.name, self.list_id)

    @staticmethod
    def create_remote_list(sender, instance, **kwargs):
        if not instance.id:
            client = EmailMarketing()
            new_list = client.create_list(instance.list_id, instance.name)
            if instance.list_id != new_list.id:
                instance.list_id = new_list.id


pre_save.connect(List.create_remote_list, List)


class Subscription(models.Model):
    list = models.ForeignKey(List)
    subscriber = models.ForeignKey(Subscriber)
    joined = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        unique_together = (('list', 'subscriber'),)

    def __str__(self):
        return "%s (%s)" % (self.subscriber, self.list)
