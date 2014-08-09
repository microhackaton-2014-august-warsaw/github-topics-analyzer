import datetime
import json
import os
import threading

from django.test import TestCase
from ghtopanal.logger import create_log_message
from ghtopanal.analyzer import analyze
from microhackaton.settings import BASE_DIR


class AnalyzeTestCase(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_parses_repositories_and_organisations(self):
        # given
        with open(os.path.join(BASE_DIR, os.path.join('ghtopanal', "test_input.json"))) as input_file:
            data = json.loads(input_file.read())

        # when
        result = analyze(data)

        # then
        self.assertEqual(result["pairId"], "2")
        self.assertEqual(result["analyzerType"], "github")
        self.assertEqual(result["analyzedId"], "jroper")
        self.assertEqual(sorted(result["topics"], key=lambda item: item['name']), [
            {
                "name": u"Java"
            }, {
                "name": u"Scala"
            }, {
                'name': u'activator'
            }, {
                'name': u'jdk-observable-future-proposal'
            }, {
                'name': u'pebbleblog'
            }, {
                'name': u'playframework'
            }, {
                'name': u'sbt'
            }, {
                'name': u'typesafehub'
            }, {
                'name': u'webjars'
            }
        ])

    def test_log_format(self):
        # given
        level = "WARN"
        message = "something something"
        correlation_id = "123"
        now = datetime.datetime(2014, 1, 2, 3, 4, 5, 7)

        # when
        log = create_log_message(level, correlation_id, message, now)

        # then
        self.assertEqual(log, "2014-01-02 03:04:05.000007Z | WARN  | 123 | " +
                         str(threading.currentThread().ident) + " | default | something something")
