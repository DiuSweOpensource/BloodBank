# Generated by Django 2.2 on 2020-04-18 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blooddonor',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='blooddonor',
            name='modified_by',
        ),
    ]
