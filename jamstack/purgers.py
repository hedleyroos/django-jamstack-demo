from copy import deepcopy

from django.conf import settings
from django.core.cache import cache
from django.urls import resolve
from django.urls.exceptions import Resolver404
from django_distill.distill import urls_to_distill
from django_distill.renderer import render_to_dir


class StdOut:
    """Simulate standard out.
    """
    def __call__(self, out):
        print(out)


def update_static_resources(path, headers=None):
    """If path is subject to django-distill then regenerate the static resource.
    """
    print("PURGER HOOK", path)
    try:
        resolved = resolve(path)
    except Resolver404:
        return

    for url in urls_to_distill:
        if url[0] == resolved.tried[-1][0]:
            copied_url = deepcopy(url)
            print("MATCH", url[0])
            # Sneak in the param set. We have a custom django-distill renderer that avoids doing
            # redundant regeneration, and this is the way we trigger that code path.
            param_set = cache.get("distill-%s" % path, None)
            setattr(copied_url[0], "param_set", param_set)
            render_to_dir(settings.JAMSTACK["output-directory"], [copied_url], StdOut())
