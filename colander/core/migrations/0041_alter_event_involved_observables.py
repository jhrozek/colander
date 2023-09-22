# Generated by Django 3.2.18 on 2023-09-20 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20230918_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='involved_observables',
            field=models.ManyToManyField(blank=True, help_text='Select the observables involved with this event.', null=True, related_name='events', to='core.Observable'),
        ),
    ]