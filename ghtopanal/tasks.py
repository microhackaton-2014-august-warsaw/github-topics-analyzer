from __future__ import absolute_import
import json

from celery import shared_task
import requests
import ghtopanal.logger

from microhackaton import sd

from ghtopanal.analyzer import analyze


@shared_task
def process(msg):
    result = analyze(msg)
    if sd is None:
        url = "http://localhost:8080"
        ghtopanal.logger.warn(result.get("pairId"), "ZooKeeper not found, using localhost:8080 as target")
    else:
        url = sd.get_instance('topics-collector')
    headers = {'Content-type': 'application/json'}
    data = json.dumps(result)
    ghtopanal.logger.debug(result.get("pairId"), "Responding to " + url + " with: " + data)
    requests.post(url, data=data, headers=headers)
