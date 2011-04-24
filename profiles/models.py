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
        ('accepted and attending', 'Accepted and Attending'),
        ('denied', 'Denied')
    )

    bring_skillsets_json = models.CharField(max_length=255, blank=True, null=True)
    need_skillsets_json = models.CharField(max_length=255, blank=True, null=True)
    past_experience_blurb = models.TextField(blank=True, null=True)
    bring_blurb = models.TextField(blank=True, null=True)
    can_start = models.CharField(max_length=25, choices = START_CHOICES, blank=True, null=True)
    idea_status = models.CharField(max_length=25, choices = IDEA_STATUS_CHOICES, blank=True, null=True)
    event_status = models.CharField(max_length=25, choices =  EVENT_STATUS_CHOICES, default = 'Pending')
    event = models.ForeignKey('Event', null=True, blank=True)

class LinkedinProfile(models.Model):
    fd_profile = models.OneToOneField("FdProfile")
    oauth_object = models.TextField(max_length=500)
    profile_raw = models.TextField()
    profile_picture = models.URLField(null=True, blank=True)
    profile_location = models.CharField(max_length=100)
    profile_industry = models.CharField(max_length=100)

class Event(models.Model):
    event_date = models.DateField()
    event_location = models.ForeignKey('EventLocation')

    def __unicode__(self):
        return '%s - %s' % (self.event_location.display, self.event_date)


class EventLocation(models.Model):
    display = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=100)

    def __unicode__(self):
        return self.display

### END of traditional models definition. Should this be moved to __init__.py?
# Listen for new accounts/updates via social auth and update the FdProfile
from social_auth.signals import pre_update
from social_auth.backends.contrib.linkedin import LinkedinBackend

def linkedin_extra_values(sender, user, response, details, **kwargs):
    """
    print "response=", response
    print "details=", details
    response= {'last-name': 'Sullivan', 'headline': 'VP of Technology at Krux Digital', 'first-name': 'Nick', 'access_token': 'oauth_token_secret=a51a3341-1e3b-4df3-a1ee-bddc4c89e499&oauth_token=8da0d321-14cc-4d9e-9cba-ee17bd952d2a', 'site-standard-profile-request': {'url': 'http://www.linkedin.com/profile?viewProfile=&key=732523&authToken=u2nf&authType=name&trk=api*a101448*s101448*'}, 'id': '732523'}
details= {'first_name': 'Nick', 'last_name': 'Sullivan', 'email': ''}
    """
    return True

pre_update.connect(linkedin_extra_values, sender=LinkedinBackend)
