from django.contrib import admin
from profiles.models import Applicant, Event, EventLocation, Interest, Skillset

class ApplicantAdmin(admin.ModelAdmin):
    list_filter = ['event']
admin.site.register(Applicant, ApplicantAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_location', 'event_date')
    list_filter = ['event_location']
    ordering = ["-event_date"]
    date_hierarchy = "event_date"
admin.site.register(Event, EventAdmin)

class EventLocationAdmin(admin.ModelAdmin):
    list_display = ('display', 'city', 'state', 'country')
    ordering = ["display"]
admin.site.register(EventLocation, EventLocationAdmin)

class SkillsetAdmin(admin.ModelAdmin):
    list_display = ('name', 'ord')
    ordering = ["ord"]
admin.site.register(Skillset, SkillsetAdmin)

class InterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'ord')
    ordering = ["ord"]
    pass
admin.site.register(Interest, InterestAdmin)
