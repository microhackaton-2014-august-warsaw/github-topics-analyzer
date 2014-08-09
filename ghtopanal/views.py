from django.shortcuts import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def analyze(request, pair_id):
    return HttpResponse(pair_id, mimetype='text/plain')
