from os import system

from django.views.generic import DetailView, ListView
from ultracache.decorators import ultracache

from jamstack import models


@ultracache(86400)
class PostListView(ListView):
    model = models.Post


@ultracache(86400)
class PostDetailView(DetailView):
    model = models.Post
