# Generated by Django 4.2.2 on 2023-07-17 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]