from django.shortcuts import HttpResponse
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseBadRequest

import requests
import json
import ghtopanal.logger
from microhackaton import sd
import ghtopanal.analyzer

@require_http_methods(["POST", "PUT"])
def analyze(request):
    if not request.body:
        ghtopanal.logger.warn("", "Request body missing")
        return HttpResponseBadRequest()

    data = json.loads(str(request.body))
    ghtopanal.logger.debug(data.get("pairId"), "Got request: " + str(data))

    class LogSuccessResponse(HttpResponse):
        def close(self):
            super(LogSuccessResponse, self).close()
            try:
                result = ghtopanal.analyzer.analyze(data)
                if sd is None:
                    url = "http://localhost:8080"
                    ghtopanal.logger.warn(result.get("pairId"), "ZooKeeper not found, using localhost:8080 as target")
                else:
                    url = sd.get_instance('topics-collector')
                headers = {'Content-type': 'application/json'}
                response = json.dumps(result)
                ghtopanal.logger.debug(result.get("pairId"), "Responding to " + url + " with: " + response)
                requests.post(url, data=response, headers=headers)
            except Exception, ex:
                print ex
                ghtopanal.logger.error(data.get("pairId"), ex)

    return LogSuccessResponse(status=202)
