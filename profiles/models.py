from django.db import models

from userena.models import UserenaBaseProfile

class FdProfile(UserenaBaseProfile):
    username   = models.CharField(max_length=100)
    last_login = models.DateTimeField(blank=True)
    is_active  = models.BooleanField(default=True)


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
