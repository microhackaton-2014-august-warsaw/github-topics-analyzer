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
    url = sd.get_instances('topics-collector')
    headers = {'Content-type': 'application/json'}
    data = json.dumps(result)
    ghtopanal.logger.debug(data.get("pairId"), "Adding to queue")
    requests.post(url, data=data, headers=headers)