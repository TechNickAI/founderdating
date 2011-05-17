from django.contrib import admin
from profiles.models import Applicant, Event, EventLocation, Interest, Skillset
import json

class ApplicantAdmin(admin.ModelAdmin):
    def linkedin_link(self, obj):
        return '<a href="%s" target="_new"><nobr><img src="/static/img/linkedin_icon.png">Profile</nobr></a>' % (obj.linkedin_url)
    linkedin_link.allow_tags = True
    linkedin_link.short_description = 'LinkedIn'

    def references(self, obj):
        out = ''
        if len(obj.recommend_json) > 1:
            jrec = json.loads(obj.recommend_json)
            for i, rec in jrec.items():
                if rec['name'] != "":
                    out += '<a href="mailto:' + rec['email'] + '">' + rec['name'] + '</a><br />'
        return out
            
    references.allow_tags = True


    list_display = ('name', 'can_start', 'idea_status', 'event_status', 'linkedin_link', 'references', 'event')
    list_filter = ['event', 'event_status', 'can_start', 'idea_status']
    list_editable = ('event_status',)
    date_hierarchy = "created_at"
    ordering = ["-created_at"]
    save_on_top = True
    search_fields = ['name', 'email']

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
