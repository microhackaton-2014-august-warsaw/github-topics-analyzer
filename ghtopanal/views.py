from django.shortcuts import HttpResponse
from django.http import HttpResponseNotAllowed


def analyze(request, pair_id):
    if request.method == 'POST':
        return HttpResponse(pair_id, mimetype='text/plain')
    else:
        return HttpResponseNotAllowed(permitted_methods=['POST'])