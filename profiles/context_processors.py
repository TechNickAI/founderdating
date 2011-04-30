from fd.profiles.models import Event, EventLocation, Skillset
import datetime

def fd_context(request):
    context = {}
    context["session"] = request.session
    context["get"] = request.GET.copy()

    # Bring in the event locations for the menu
    context["event_locations"] = EventLocation.objects.all()

    # Upcoming events for whever ever they are needed
    context["upcoming_events"] = Event.objects.filter(event_date__gte=datetime.datetime.now())

    # Skillsets for whever ever they are needed
    context["skillsets"] = Skillset.objects.all().order_by("ord")

    return context
