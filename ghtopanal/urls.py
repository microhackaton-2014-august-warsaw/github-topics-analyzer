from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'(?P<pair_id>)[0-9]+/?$', views.analyze),
)
