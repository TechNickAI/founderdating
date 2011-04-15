def fd_context(request):
	context = {}
	context["session"] = request.session
	context["get"] = request.GET.copy()
	return context
