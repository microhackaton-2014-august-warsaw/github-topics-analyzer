import json
import os

from django.test import TestCase
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
