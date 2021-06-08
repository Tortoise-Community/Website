# Generated by Django 3.0.7 on 2020-10-21 18:32

import django.contrib.postgres.fields.jsonb
from django.db import migrations
import utils.misc


class Migration(migrations.Migration):

    dependencies = [
        ('websitedata', '0008_remove_events_sponsors'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='sponsors',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=utils.misc.empty_dict, null=True),
        ),
    ]