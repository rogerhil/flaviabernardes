import importlib

from django.conf import settings
from django.contrib.sitemaps import ping_google
from django.core.mail import send_mail
from django.db import models


class CmsObject(object):

    class cms:
        """ Must define the following attributes, e.g:
        draft_class = 'blog.Draft'
        """

    @property
    def draft_class(self):
        klass = self.cms.draft_class
        if isinstance(klass, str):
            app, model = klass.split('.')
            module = importlib.import_module('flaviabernardes.%s.models' % app)
            klass = getattr(module, model)
        return klass

    @property
    def draft_model_name(self):
        return self.draft_class._meta.model_name

    @property
    def model_name(self):
        return self._meta.model_name

    def new_draft(self):
        draft = self.draft_class()
        many_to_many = {}
        for field in self._meta.fields:
            attr_name = field.name
            if attr_name == 'id':
                continue
            attr = getattr(self, field.name)
            if isinstance(field, models.fields.related.ManyToManyField):
                many_to_many[attr_name] = attr
                continue
            setattr(draft, attr_name, attr)
        draft.instance = self
        draft.save()

        # save many to many relation
        for attr_name, attr in many_to_many.items():
            for item in getattr(self, attr_name).all():
                getattr(draft, attr_name).add(item)

        draft.save()
        return draft


class CmsDraft(object):

    class cms:
        """ Must define the following attributes, e.g:
        draft_related_class = Post
        instance_name = 'post'
        """

    class TooOldToPublish(Exception):
        pass

    @property
    def model_name(self):
        return self._meta.model_name

    @property
    def draft_related_class(self):
        klass = self.cms.draft_related_class
        if isinstance(klass, str):
            klass = __import__(klass)
        return klass

    @property
    def instance(self):
        return getattr(self, self.cms.instance_name)

    @instance.setter
    def instance(self, value):
        setattr(self, self.cms.instance_name, value)

    def publish(self, publish_old=False):
        if not publish_old:
            if self.__class__.objects.filter(created__gt=self.created).count():
                raise self.__class__.TooOldToPublish('There are more recent'
                                                     'drafts created than '
                                                     'this one.')
        instance = self.instance
        new = False
        many_to_many = {}
        if instance is None:
            new = True
            instance = self.draft_related_class()

        for field in instance._meta.fields:
            attr_name = field.name
            if attr_name == 'id':
                continue
            attr = getattr(self, field.name)
            if isinstance(field, models.fields.related.ManyToManyField):
                many_to_many[attr_name] = attr
                continue
            setattr(instance, attr_name, attr)

        self.instance = instance
        self.instance.save()

        for attr_name, attr in many_to_many.items():
            for item in getattr(self, attr_name).all():
                getattr(self.instance, attr_name).add(item)

        self.instance.save()

        try:
            ping_google()
        except Exception as err:
            subj = 'Flavia Bernardes Art: Error while trying to ping_google()'
            send_mail(subj, str(err), settings.SERVER_EMAIL,
                      [e[1] for e in settings.ADMINS])
