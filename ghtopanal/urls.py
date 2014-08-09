from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'(?P<pair_id>\d+)/(?P<user_id>\w+)/?$', views.analyze),
)
