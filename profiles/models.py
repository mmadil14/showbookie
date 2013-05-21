from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    bio = models.TextField(blank=True, default='')
    facebook = models.CharField('Facebook Username', max_length=30, blank=True, default='')
    twitter = models.CharField('Twitter Username', max_length=30, blank=True, default='')

    # To add purchase details once. The purchase model is completed.

    def __unicode__(self):
        return self.user.username
