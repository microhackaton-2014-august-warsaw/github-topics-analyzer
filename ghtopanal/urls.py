from django.conf.urls import patterns, url

from . import views

import logger

logger.info("", "Starting application")

urlpatterns = patterns('',
    url(r'analyze/?$', views.analyze),
)
