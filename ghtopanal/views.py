from django.shortcuts import HttpResponse
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseBadRequest

from .tasks import *

@require_http_methods(["POST"])
def analyze(request, pair_id, user_id):
    if not request.body:
        return HttpResponseBadRequest()
    process.delay(pair_id, user_id, str(request.body))
    return HttpResponse(status=202)
