# Generated by Django 4.2.2 on 2023-07-26 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_alter_eventregistration_event_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventregistration',
            name='event',
        ),
        migrations.AddField(
            model_name='organizer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
