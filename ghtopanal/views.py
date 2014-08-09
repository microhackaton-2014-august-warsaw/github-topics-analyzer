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
    ghtopanal.logger.debug("", "Analyze called with" + str(request.body))
    process.delay(str(request.body))
    return HttpResponse(status=202)
