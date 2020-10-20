# Generated by Django 3.0.7 on 2020-10-20 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websitedata', '0004_auto_20201021_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='page_theme',
            field=models.CharField(choices=[('event-light-theme', 'Light Theme'), ('event-dark-theme', 'Dark Theme'), ('event-ares-theme', 'Ares Theme'), ('event-nemesis-theme', 'Nemesis Theme'), ('event-grass-hopper-theme.css', 'Grasshopper Theme')], default='event-light-theme', max_length=35),
        ),
    ]
