from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


class UserPosition(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class UserSector(models.Model):
    name = models.CharField(max_length=128)
    tags = models.ManyToManyField()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Full Name'), blank=True, max_length=255)
    position = models.OneToOneField(UserPosition, null=True, blank=True, max_length=255)
    sector = models.ForeignKey(UserSector, null=True, blank=True, max_length=255)
    number = models.BigIntegerField(blank=True, null=True, help_text="Enter the number with country code.")
    image = models.ImageField(upload_to='uploads/', default='uploads/default_image.png')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
