from django.db import models

# Create your models here.


class Office(models.Model):
    name = models.CharField(max_length=128)
