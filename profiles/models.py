from django.db import models
from userena.models import UserenaBaseProfile

class FdProfile(UserenaBaseProfile):
    START_CHOICES = (
        ('immediately', 'Immediately'),
        ('part now full soon', 'Part-time now, full-time soon'),
        ('part now full if no suck', 'Part-time now, full-time if it takes off'),
        ('later', 'I don\'t have much for the next several months')
    )
    IDEA_STATUS_CHOICES = (
        ('straight', 'I have an idea that I\'m committed to'),
        ('curious', 'I have and idea, but I\'m also open to exploring other ideas'),
        ('ambiguous', 'I don\'t yet have an idea')
    )
    EVENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('checking references', 'Checking References'),
        ('awaiting interview', 'Awaiting Interview'),
        ('accepted and attending', 'Accepted & Attending'),
        ('denied', 'Denied')
    )
    FOUNDER_TYPE_CHOICES = (
        ('technical', 'Tech'),
        ('business', 'Biz')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)
    bring_skillsets_json = models.TextField(blank=True, null=True)
    need_skillsets_json = models.TextField(blank=True, null=True)
    interests_json = models.TextField(blank=True, null=True)
    past_experience_blurb = models.TextField(blank=True, null=True)
    bring_blurb = models.TextField(blank=True, null=True)
    building_blurb = models.TextField(blank=True, null=True)
    can_start = models.CharField(max_length=25, choices = START_CHOICES, blank=True, null=True)
    idea_status = models.CharField(max_length=25, choices = IDEA_STATUS_CHOICES, blank=True, null=True)
    event_status = models.CharField(max_length=25, choices =  EVENT_STATUS_CHOICES, default = 'Pending')
    founder_type = models.CharField(max_length=15, choices =  FOUNDER_TYPE_CHOICES, null=True, blank=True)
    linkedin_url = models.URLField(blank=True, null=True)
    event = models.ForeignKey('Event', null=True, blank=True)
    comments = models.TextField(blank=True, null=True)

class Applicant(models.Model):
    GROUP_CHOICES = []
    i = 0
    while i < 10:
        i += 1
        GROUP_CHOICES.append((i,i))

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    # Effectively a copy of FdProfile
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)
    bring_skillsets_json = models.TextField(blank=True, null=True, verbose_name="Skillsets brought")
    need_skillsets_json = models.TextField(blank=True, null=True, verbose_name="Skillsets needed")
    recommend_json = models.TextField(blank=True, null=True, verbose_name="Recommendations")
    interests_json = models.TextField(blank=True, null=True, verbose_name="Interests")
    past_experience_blurb = models.TextField(blank=True, null=True, verbose_name="Past experience")
    bring_blurb = models.TextField(blank=True, null=True, verbose_name="What they bring")
    building_blurb = models.TextField(blank=True, null=True, verbose_name="What they want to build")
    can_start = models.CharField(max_length=25, choices = FdProfile.START_CHOICES, blank=True, null=True)
    idea_status = models.CharField(max_length=25, choices = FdProfile.IDEA_STATUS_CHOICES, blank=True, null=True)
    event_status = models.CharField(max_length=25, choices =  FdProfile.EVENT_STATUS_CHOICES, default = 'Pending')
    founder_type = models.CharField(max_length=15, choices =  FdProfile.FOUNDER_TYPE_CHOICES, null=True, blank=True)
    linkedin_url = models.URLField(blank=True, null=True)
    event = models.ForeignKey('Event', null=True, blank=True)
    event_group = models.PositiveSmallIntegerField(null=True, blank=True, choices=GROUP_CHOICES)
    comments = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '%s - %s - %s' % (self.name, self.event.event_location.display, self.event.event_date)
    

class Recommendation(models.Model):
    fdprofile = models.ForeignKey('FdProfile')
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    

class LinkedinProfile(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)
    fd_profile = models.OneToOneField("FdProfile")
    oauth_object = models.TextField(max_length=500)
    profile_raw = models.TextField()
    profile_picture = models.URLField(null=True, blank=True)
    profile_location = models.CharField(max_length=100)
    profile_industry = models.CharField(max_length=100)
    connections_raw = models.TextField()

class Event(models.Model):
    event_date = models.DateField()
    event_location = models.ForeignKey('EventLocation')
    description = models.TextField(max_length=1000)
    apply_deadline = models.DateField()

    def __unicode__(self):
        return '%s, %s' % (self.event_location.city, self.event_date.strftime('%b %Y'))


class EventLocation(models.Model):
    display = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=100)

    def __unicode__(self):
        return self.display

class Skillset(models.Model):
    name = models.CharField(max_length=100)
    ord = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.name

class Interest(models.Model):
    name = models.CharField(max_length=100)
    ord = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.name



### END of traditional models definition. Should this be moved to __init__.py?
# Listen for new accounts/updates via social auth and update the FdProfile
from social_auth.signals import pre_update
from social_auth.backends.contrib.linkedin import LinkedinBackend

def linkedin_extra_values(sender, user, response, details, **kwargs):
    """
    print "response=", response
    print "details=", details
    response= {'last-name': 'Sullivan', 'headline': 'VP of Technology at Krux Digital', 'first-name': 'Nick', 'access_token': 'oauth_token_secret=xxxxx', 'site-standard-profile-request': {'url': 'http://www.linkedin.com/profile?viewProfile=&key=732523&authToken=u2nf&authType=name&trk=api*a101448*s101448*'}, 'id': '732523'}
details= {'first_name': 'Nick', 'last_name': 'Sullivan', 'email': ''}
    """
    return True

pre_update.connect(linkedin_extra_values, sender=LinkedinBackend)
