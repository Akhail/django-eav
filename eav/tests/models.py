from builtins import object
from django.db import models
from ..decorators import register_eav

class Patient(models.Model):
    class Meta(object):
        app_label = 'eav'

    name = models.CharField(max_length=12)

    def __unicode__(self):
        return self.name

class Encounter(models.Model):
    class Meta(object):
        app_label = 'eav'

    num = models.PositiveSmallIntegerField()
    patient = models.ForeignKey(Patient)

    def __unicode__(self):
        return '%s: encounter num %d' % (self.patient, self.num)

@register_eav()
class ExampleModel(models.Model):
    class Meta(object):
        app_label = 'eav'

    name = models.CharField(max_length=12)

    def __unicode__(self):
        return self.name
