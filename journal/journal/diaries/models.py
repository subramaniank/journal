from django.db import models
from jsonfield.fields import JSONField
from accounts.models import JournalWriter


class Diary(models.Model):

    writer = models.ForeignKey(JournalWriter, related_name='diaries')
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    place = models.CharField(max_length=100, null=True)

    created_on = models.BigIntegerField()
    updated_on = models.BigIntegerField()
    extra_params = JSONField(default={})

