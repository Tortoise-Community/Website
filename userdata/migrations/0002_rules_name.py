# Generated by Django 3.0.7 on 2020-09-17 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rules',
            name='name',
            field=models.CharField(default='Rule name', max_length=20, null=True),
        ),
    ]