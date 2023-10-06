from django.contrib import admin
from django.urls import path, re_path

from apps.menu.views import index, main

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    re_path(r'^(?P<slugs>[\w-]+/)+$', main)
]
