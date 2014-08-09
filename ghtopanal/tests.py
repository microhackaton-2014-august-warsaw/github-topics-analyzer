import json

from django.test import TestCase
from analyzer import analyze


class AnalyzeTestCase(TestCase):
    def test_parses_repositories_and_organisations(self):
        # given
        input = None
        with open("test_input.json") as input_file:
            input = json.loads(input_file.read())

        # when
        result = list(analyze(input))

        # then
        self.assertEqual(sorted(result), [
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
