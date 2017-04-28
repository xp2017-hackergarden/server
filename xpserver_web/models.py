from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    activation_code = models.CharField(max_length=255, default="0000")
    fcm_registration_id = models.CharField(max_length=255, blank=True)

    def __str__(self):
        if self.user:
            if self.fcm_registration_id:
                return '%s - profile with activated mobile app.' % self.user.username
            else:
                return '%s - profile.' % self.user.username
        else:
            return 'Profile unknown user'
