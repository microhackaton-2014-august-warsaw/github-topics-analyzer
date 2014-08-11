from __future__ import absolute_import

from service_discovery import ServiceDiscovery

from.logger import error

try:
    sd = ServiceDiscovery('/pl/pl/microhackaton', 'zookeeper.microhackathon.pl:2181')
except Exception as ex:
    error('INIT', str(ex))
    sd = None
