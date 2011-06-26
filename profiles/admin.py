from django.contrib import admin
from django.core.mail import EmailMessage
from profiles.models import Applicant, EmailTemplate, Event, EventLocation, Interest, Skillset
import json

    
class ApplicantAdmin(admin.ModelAdmin):
    def linkedin_link(self, obj):
        return '<a href="%s" target="_new"><nobr><img src="/static/img/linkedin_icon.png">Profile</nobr></a>' % (obj.linkedin_url)
    linkedin_link.allow_tags = True
    linkedin_link.short_description = 'LinkedIn'

    class Media:
        js = (
            "js/fd_applicant_admin.js", # first because it puts jquery back into main name space
            "js/jquery-ui-1.8.13.min.js"
        )
        css = {
            "all": ("css/jquery-ui-1.8.13.custom.css", "css/admin.css",)
        }

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

    def bulk_email(self, request, queryset):
        emails_sent = 0
        email = EmailMessage(
            subject = request.POST.get("subject"),
            body = request.POST.get("message"),
            bcc = request.POST.get("bcc"),
            from_email = request.POST.get("from"))

        for applicant in queryset:
            email.to = [request.POST.get("override_to", applicant.email)]
            email.send()
            emails_sent += 1
        
        self.message_user(request, "%s e-mails sent" % emails_sent)

    def email_references(self, request, queryset):
        emails_sent = 0
        queryset.update(event_status="checking references")
    email_references.short_description = "Email the references for the selected applicants"

    def email_declination(self, request, queryset):
        queryset.update(event_status="denied")
        self.bulk_email(request, queryset)
    email_declination.short_description = "Email a declination to selected applicants"

    def invite_to_event(self, request, queryset):
        self.bulk_email(request, queryset)
    invite_to_event.short_description = "Invite the selected candidates to event"
        
    def email_applicant(self, request, queryset):
        self.bulk_email(request, queryset)
    email_applicant.short_description = "Email selected applicants"


    list_display = ('name', 'event_status', 'founder_type', 'event_group', 'linkedin_link', 'references', 'comments')
    list_filter = ['event', 'event_status', 'founder_type', 'event_group', 'can_start', 'idea_status']
    list_editable = ('founder_type', 'event_group', 'event_status', 'comments')
    date_hierarchy = "created_at"
    ordering = ["-created_at"]
    save_on_top = True
    list_select_related = True
    search_fields = ['name', 'email']
    actions = [email_references, email_declination, invite_to_event, email_applicant]
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
admin.site.register(Interest, InterestAdmin)

class EmailTemplateAdmin(admin.ModelAdmin):
    search_fields = ['name', 'subject', 'message']
admin.site.register(EmailTemplate, EmailTemplateAdmin)
