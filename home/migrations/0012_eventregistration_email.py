# Generated by Django 4.2.2 on 2023-08-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_eventfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregistration',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
