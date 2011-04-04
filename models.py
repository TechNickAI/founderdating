from userena.models import UserenaBaseProfile

class MyProfile(UserenaBaseProfile):
    favourite_snack = models.CharField(_('favourite snack'),
                                       max_length=5)
