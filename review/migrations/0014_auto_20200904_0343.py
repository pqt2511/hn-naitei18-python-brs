# Generated by Django 3.1.1 on 2020-09-04 03:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0013_merge_20200904_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='request',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
