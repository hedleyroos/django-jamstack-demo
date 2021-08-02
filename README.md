Django Jamstack Demo
====================
**Generate static resources from a Django site using django-ultracache and django-distill. Supports partial regeneration and scales to millions of objects.**

Usage
-----

Start the containers::

    DOCKER_BUILDKIT=1 docker-compose up --build

Visit http://192.168.18.10/. Open Post One and Post Two in new tabs. Note all the files are served
directly from Nginx. Make a note of the ``Generated`` values.

Modify Post One::

    docker exec -ti django-jamstack-demo_app_1 python manage.py edit_first_post

Reload the browser tabs. The index page and Post One has a new ``Generated`` value, but Post Two
has remained untouched.

