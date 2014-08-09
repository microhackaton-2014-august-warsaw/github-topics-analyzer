from django.shortcuts import HttpResponse
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseBadRequest

from .tasks import *
import ghtopanal.logger

@require_http_methods(["POST", "PUT"])
def analyze(request):
    if not request.body:
        ghtopanal.logger.warn("", "Request body missing")
        return HttpResponseBadRequest()
    data = json.loads(str(request.body))
    ghtopanal.logger.debug(data.get("pairId"), "Queuing request: " + str(data))
    process.delay(data)
    return HttpResponse(status=202)
