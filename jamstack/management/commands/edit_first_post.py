from django.core.management.base import BaseCommand

from jamstack import models


class Command(BaseCommand):

    def handle(self, *args, **options):
        models.Post.objects.get(pk=1).save()
