# Generated by Django 3.0.2 on 2020-03-11 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0004_auto_20200311_0649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopprofile',
            old_name='email',
            new_name='email_address',
        ),
    ]