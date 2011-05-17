from django.contrib import admin
from profiles.models import Applicant, Event, EventLocation, Interest, Skillset

class ApplicantAdmin(admin.ModelAdmin):
    def linkedin_link(self, obj):
        return '<a href="%s" target="_new"><nobr><img src="/static/img/linkedin_icon.png">Profile</nobr></a>' % (obj.linkedin_url)

    linkedin_link.allow_tags = True
    linkedin_link.short_description = 'LinkedIn'

    list_display = ('name', 'email', 'can_start', 'idea_status', 'event_status', 'linkedin_link', 'event')
    list_filter = ['event', 'event_status', 'can_start', 'idea_status']
    date_hierarchy = "created_at"
    ordering = ["-created_at"]
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
