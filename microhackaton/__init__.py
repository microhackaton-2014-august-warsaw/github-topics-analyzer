from __future__ import absolute_import

from service_discovery import ServiceDiscovery

try:
    sd = ServiceDiscovery('/pl/pl/microhackaton', 'zookeeper.microhackathon.pl:2181')
except Exception, ex:
    print ex
    sd = None
