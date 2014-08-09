from __future__ import absolute_import
import json

from celery import shared_task
import requests

from microhackaton import sd

from ghtopanal.analyzer import analyze


@shared_task
def process(msg):
    result = analyze(msg)
    url = sd.get_instances('topics-collector')
    headers = {'Content-type': 'application/json'}
    requests.post(url, data=json.dumps(result), headers=headers)