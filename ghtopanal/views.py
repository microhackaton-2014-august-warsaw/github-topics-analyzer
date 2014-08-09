from django.shortcuts import HttpResponse
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseBadRequest

from .tasks import *

@require_http_methods(["POST"])
def analyze(request):
    if not request.body:
        return HttpResponseBadRequest()
    process.delay(str(request.body))
    return HttpResponse(status=202)
