# Generated by Django 3.0.2 on 2020-03-11 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0003_auto_20200311_0639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopprofile',
            old_name='address_line1',
            new_name='address_line_1',
        ),
        migrations.RenameField(
            model_name='shopprofile',
            old_name='address_line2',
            new_name='address_line_2',
        ),
        migrations.RenameField(
            model_name='shopprofile',
            old_name='address_line3',
            new_name='address_line_3',
        ),
        migrations.RenameField(
            model_name='shopprofile',
            old_name='description',
            new_name='shop_details',
        ),
    ]
