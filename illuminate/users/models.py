from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):



    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Full Name'), blank=True, max_length=255)
    # position = models.CharField(_('Position'), null=True, blank=True, max_length=255)
    # team = models.CharField(_('Team'), null=True, blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
