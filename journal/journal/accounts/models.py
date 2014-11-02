from django.contrib.auth.models import User
from django.db import models
from jsonfield.fields import JSONField


class JournalWriter(models.Model):

    user = models.OneToOneField(to=User, primary_key=True)
    phone = models.CharField(max_length=15, null=True)
    status = models.CharField(max_length=30)

    created_on = models.BigIntegerField()
    updated_on = models.BigIntegerField()
    extra_params = JSONField(default={})