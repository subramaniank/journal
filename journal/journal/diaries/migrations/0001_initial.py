# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('content', models.TextField(null=True)),
                ('place', models.CharField(max_length=100, null=True)),
                ('created_on', models.BigIntegerField()),
                ('updated_on', models.BigIntegerField()),
                ('extra_params', jsonfield.fields.JSONField(default={})),
                ('writer', models.ForeignKey(related_name='diaries', to='accounts.JournalWriter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
