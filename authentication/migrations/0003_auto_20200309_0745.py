# Generated by Django 3.0.4 on 2020-03-09 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20200309_0625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='full_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('SHOPKEEPER', 'shopekeeper'), ('DELIVERY_PERSON', 'delivery person'), ('CUSTOMER', 'customer')], default='CUSTOMER', max_length=20, verbose_name='user role'),
        ),
    ]
