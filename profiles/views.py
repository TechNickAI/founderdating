from django.shortcuts import render_to_response
from django.template import RequestContext

def attend(request):
    c = {}
    return render_to_response('attend.html', c, context_instance=RequestContext(request))


def events(request):
    c = {}
    return render_to_response('events.html', c, context_instance=RequestContext(request))
