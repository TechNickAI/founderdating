# Authentication with the old founder dating backend, to be used for transitioning.
# Validate the password with the old PHP method. If it passes, convert the user to 
# a "new" account by changing the password to the django method.
#
# This always returns None, so the django method will be called next.

from django.contrib.auth.models import User
import subprocess
import settings

class LegacyBackend:
    supports_object_permissions = False
    supports_anonymous_user = False

    def authenticate(self, username=None, password=None):
        users = User.objects.filter(username=username)
        if len(users) < 1:
            # No matching user
            return None

        u = users[0]
        if '$' in u.password:
            # It's already a django style password, not the old fd style.
            return None

        # Exec out to the php auth to validate
        old_valid = subprocess.call(['php', settings.ROOT_PATH + '/oldfd/Auth.php', password, u.password])

        if old_valid == 0:
            # if found, reset to django style password
            u.set_password(password)
            u.save()
        
        return None
