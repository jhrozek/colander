# Generated by Django 3.2.15 on 2022-12-11 14:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20221211_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='observable',
            name='classification',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='observable',
            name='raw_value',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='es_prefix',
            field=models.CharField(default='nnnm078lqgt24s2b', editable=False, max_length=16),
        ),
        migrations.AlterField(
            model_name='event',
            name='first_seen',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 11, 14, 10, 12, 769327, tzinfo=utc), help_text='First time the event has occurred.'),
        ),
        migrations.AlterField(
            model_name='event',
            name='last_seen',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 11, 14, 10, 12, 769350, tzinfo=utc), help_text='First time the event has occurred.'),
        ),
        migrations.AlterField(
            model_name='observable',
            name='es_prefix',
            field=models.CharField(default='bf7q9d8v629mobtf', editable=False, max_length=16),
        ),
    ]
