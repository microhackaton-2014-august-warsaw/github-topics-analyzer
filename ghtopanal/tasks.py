from __future__ import absolute_import
import json

from celery import shared_task
import requests

from microhackaton import sd


@shared_task
def process(pair_id, user_id, msg):

    topics = ['a', 'b', 'c']

    result = {
        'pairId': pair_id,
        'analyzerType': 'github',
        'analyzedId': user_id,
        'topics': [{'name': topic} for topic in topics]
    }

    url = sd.get_instances('topics-collector')
    headers = {'Content-type': 'application/json'}
    requests.post(url, data=json.dumps(result), headers=headers)