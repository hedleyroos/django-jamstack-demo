from django.apps import AppConfig
from django_distill.distill import urls_to_distill


class MicroSiteConfig(AppConfig):
    name = "jamstack"
    verbose_name = "Jamstack"
    label = "jamstack"

    def ready(self):
        print("READY")
        print("URL", urls_to_distill)
