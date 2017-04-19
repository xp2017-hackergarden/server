from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    activation_code = models.CharField(max_length=255, default="0000")

    def __str__(self):
        if self.user:
            return 'Profile for %s' % self.user.username
        else:
            return 'Profile unknown user'
