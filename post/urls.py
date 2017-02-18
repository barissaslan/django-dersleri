from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^index/$', post_index),

    url(r'^detail/$', post_detail),

    url(r'^create/$', post_create),

    url(r'^update/$', post_update),

    url(r'^delete/$', post_delete),
]
