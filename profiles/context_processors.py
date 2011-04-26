from fd.profiles.models import Event, EventLocation
import datetime

def fd_context(request):
    context = {}
    context["session"] = request.session
    context["get"] = request.GET.copy()

    # Bring in the event locations for the menu
    context["event_locations"] = EventLocation.objects.all()

    # Upcoming events for whever ever they are needed
    context["upcoming_events"] = Event.objects.filter(event_date__gte=datetime.datetime.now())
    return context
