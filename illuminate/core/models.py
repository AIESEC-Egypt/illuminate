from django.db import models

# Create your models here.


class Office(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    parent_office = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    # Entity Type
    entity_type_choices = (
        ('AI', 'AIESEC INTERNATIONAL'),
        ('RE', 'Regional'),
        ('MC', 'Members Committee'),
        ('LC', 'Local Committee'),
        ('XX', 'Type Unknown')
    )
    entity_type = models.CharField(max_length=2, choices=entity_type_choices, default='XX')

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, id, name, entity_type):
        office = cls(id=id, name=name, entity_type=entity_type)
        return office

class AccessToken(models.Model):
    value = models.TextField()

    def __str__(self):
        return 'Access Token ' + str(self.id)

    class Meta:
        verbose_name = 'Access Token'
        verbose_name_plural = 'Access Token'
