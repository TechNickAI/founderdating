from django.db import models

from userena.models import UserenaBaseProfile

class FdProfile(UserenaBaseProfile):
    username   = models.CharField(max_length=100)
    last_login = models.DateTimeField(blank=True)
    is_active  = models.BooleanField(default=True)
