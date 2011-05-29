from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.http import require_POST
from profiles.models import Applicant, Event, FdProfile
import json

def attend(request):
    c = {
        "three": [1,2,3], 
        "idea_status_choices": dict(FdProfile.IDEA_STATUS_CHOICES),
        "start_choices": dict(FdProfile.START_CHOICES),
    }
    return render_to_response('attend.html', c, context_instance=RequestContext(request))

@require_POST
def attend_save(request):
    e = Event.objects.filter(pk = request.POST.get("event_id", -1))
    if len(e) < 1:
        raise Exception("Invalid Event")

    interests = (request.POST.getlist("interests"))
    if request.POST.get("interests_more"):
        for i in request.POST.get("interests_more").split(","):
            interests.append(i)
   
    recommend = []
    recommend_names = request.POST.getlist("recommend_name")
    recommend_emails = request.POST.getlist("recommend_email")
    for i in [0,1,2]:
        recommend.append({"name": recommend_names[i], "email": recommend_emails[i]})
    
    applicant = Applicant(
        name=request.POST.get("name"),
        email=request.POST.get("email"),
        event=e[0],
        bring_skillsets_json = json.dumps(request.POST.getlist("bring_skillsets")),
        past_experience_blurb = request.POST.get("past_experience_blurb"),
        linkedin_url = request.POST.get("linkedin_url"),
        bring_blurb = request.POST.get("bring_blurb"),
        building_blurb = request.POST.get("building_blurb"),
        interests_json = json.dumps(interests),
        can_start = request.POST.get("can_start"),
        idea_status = request.POST.get("idea_status"),
        need_skillsets_json = json.dumps(request.POST.getlist("need_skillsets")),
        recommend_json = json.dumps(recommend)
    )
    applicant.save()
    
    return redirect("/attend/thanks")

def attend_thanks(request):
    c = {}
    return render_to_response('attend_thanks.html', c, context_instance=RequestContext(request))

def events(request):
    c = {}
    return render_to_response('events.html', c, context_instance=RequestContext(request))
