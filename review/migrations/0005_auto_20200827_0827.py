# Generated by Django 2.1.1 on 2020-08-27 01:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0004_auto_20200826_1043'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bookmark',
            unique_together={('book', 'user')},
        ),
    ]