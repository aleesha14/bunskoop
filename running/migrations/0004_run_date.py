# Generated by Django 4.0.6 on 2022-11-04 21:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('running', '0003_run_track'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 4, 21, 40, 23, 366073)),
        ),
    ]
