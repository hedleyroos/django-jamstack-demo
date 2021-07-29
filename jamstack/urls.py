"""jamstack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django_distill import distill_path
from django_distill.distill import urls_to_distill

from jamstack import models, views


def get_index():
    # The index URI path, '', contains no parameters, named or otherwise.
    # You can simply just return nothing here.
    return None


def get_all_posts():
    for post in models.Post.objects.all():
        yield {"pk": post.pk}


urlpatterns = [
    path("admin/", admin.site.urls),
    distill_path("", views.PostListView.as_view(), name="post-list", distill_func=get_index, distill_file="index.html"),
    distill_path("<int:pk>/", views.PostDetailView.as_view(), name="post-detail", distill_func=get_all_posts),
]
