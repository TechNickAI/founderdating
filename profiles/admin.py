from django.contrib import admin
from profiles.models import Applicant, Event, EventLocation, Interest, Skillset
import json

    
class ApplicantAdmin(admin.ModelAdmin):
    def linkedin_link(self, obj):
        return '<a href="%s" target="_new"><nobr><img src="/static/img/linkedin_icon.png">Profile</nobr></a>' % (obj.linkedin_url)
    linkedin_link.allow_tags = True
    linkedin_link.short_description = 'LinkedIn'

    class Media:
        js = ("js/fd_applicant_admin.js",)

    def references(self, obj):
        out = ''
        if len(obj.recommend_json) > 1:
            jrec = json.loads(obj.recommend_json)
            for rec in jrec:
                if rec['name'] != "":
                    if len(rec['name']) > 25:
                        name = rec['name'][:25] + "..."
                    else:
                        name = rec['name']
                    out += '<a href="mailto:' + rec['email'] + '">' + name + '</a><br />'
        return out
    references.allow_tags = True

    def email_references(modeladmin, request, queryset):
        pass
    email_references.short_description = "Email the references for the selected applicants"

    def email_declination(modeladmin, request, queryset):
        pass
    email_declination.short_description = "Email a declination to  selected applicants"

    def invite_to_event(modeladmin, request, queryset):
        pass
    invite_to_event.short_description = "Invite the selected candidates to event"
        

    list_display = ('name', 'event_status', 'founder_type', 'event_group', 'linkedin_link', 'references', 'event')
    list_filter = ['event', 'event_status', 'founder_type', 'event_group', 'can_start', 'idea_status']
    list_editable = ('founder_type', 'event_group', 'event_status')
    date_hierarchy = "created_at"
    ordering = ["-created_at"]
    save_on_top = True
    list_select_related = True
    search_fields = ['name', 'email']
    actions = [email_references, email_declination, invite_to_event]
    radio_fields  = {"founder_type": admin.HORIZONTAL}

    fieldsets = (
        ("Basic", {
            'fields': ('name', 'email', 'linkedin_url')
        }),
        ('Event Categorization', {
            'fields': ('event', 'event_status', 'founder_type', 'event_group')
        }),
        ('Bio', {
            'fields': ('can_start', 'idea_status', 'bring_skillsets_json', 'need_skillsets_json', 'recommend_json', 'interests_json', 'past_experience_blurb', 'bring_blurb', 'building_blurb')
        })
    )
    
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
