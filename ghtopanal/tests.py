import json

from django.test import TestCase
from analyzer import analyze


class AnalyzeTestCase(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_parses_repositories_and_organisations(self):
        # given
        with open("test_input.json") as input_file:
            data = json.loads(input_file.read())

        # when
        result = analyze(data)

        # then
        self.assertEqual(result["pairId"], "2")
        self.assertEqual(result["analyzerType"], "github")
        self.assertEqual(result["analyzedId"], "jroper")
        self.assertEqual(sorted(result["topics"]), [
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
