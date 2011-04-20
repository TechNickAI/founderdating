from fd.profiles.models import EventLocation

def fd_context(request):
    context = {}
    context["session"] = request.session
    context["get"] = request.GET.copy()

    # Bring in the event locations for the menu
    context["event_locations"] = EventLocation.objects.all()
    return context
