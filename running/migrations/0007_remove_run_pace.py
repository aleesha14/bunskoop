# Generated by Django 4.0.6 on 2022-11-05 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('running', '0006_alter_run_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='run',
            name='pace',
        ),
    ]
