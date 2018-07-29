from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):
    name = "flytrap.forums"
    label = "flytrap_forums"
    verbose_name = "Pinax Fourms"

    def ready(self):
        import_module("flytrap.forums.receivers")
