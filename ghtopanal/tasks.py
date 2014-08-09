from __future__ import absolute_import

from celery import shared_task


@shared_task
def process(pair_id, user_id, msg):

    topics = ['a', 'b', 'c']

    result = {
        'pairId': pair_id,
        'analyzerType': 'github',
        'analyzedId': user_id,
        'topics': [{'name': topic} for topic in topics]
    }