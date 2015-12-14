# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import django_markdown.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_level_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='time',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 12, 12, 18, 0, 34, 361800, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='level',
            name='question',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
