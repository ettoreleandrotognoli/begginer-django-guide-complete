# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_topic_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='last_updataed',
            new_name='last_updated',
        ),
    ]
