import os
import inspect
from importlib import import_module

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flaviabernardes.settings")

import django
django.setup()

from django.conf import settings
from django.db import models
from image_cropping import ImageRatioField


def clear_old_images():
    modules = ["%s.models" % a for a in settings.INSTALLED_APPS
               if a.startswith('flaviabernardes')]
    path = os.path.join(settings.MEDIA_ROOT, settings.UPLOAD_TO)
    all_files = os.listdir(path)
    files = set()
    for module in modules:
        module = import_module(module)
        all_models = [getattr(module, i) for i in dir(module)
                      if inspect.isclass(getattr(module, i)) and
                         issubclass(getattr(module, i), models.Model) and
                         hasattr(getattr(module, i), 'objects')]
        for model in all_models:
            for obj in model.objects.all():
                for field in obj._meta.fields:
                    if not isinstance(field, ImageRatioField):
                        continue
                    fn = getattr(obj, field.image_field).name.split('/')[-1]
                    p = getattr(obj, field.name)
                    if not p:
                        continue
                    s = "%sx%s" % (field.width, field.height)
                    for filename in all_files:
                        if fn and (fn == filename or
                                   (fn in filename and p in filename and
                                    s in filename)):
                            files.add(filename)
    for filename in all_files:
        if filename in files:
            continue
        print("Removing %s..." % filename)
        os.remove(os.path.join(path, filename))


if __name__ == '__main__':
    clear_old_images()
