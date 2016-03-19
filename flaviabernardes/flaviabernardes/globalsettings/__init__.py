
from .models import GlobalSettings


def get_global_settings():
    return GlobalSettings.get()
