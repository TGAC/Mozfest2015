from django.conf.urls import patterns, include, url
from django.contrib import admin
from web.views import upload_image

urlpatterns = patterns('',
    url(r'^upload/', upload_image, name='upload_image'),
)