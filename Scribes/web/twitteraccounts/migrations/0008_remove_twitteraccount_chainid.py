# Generated by Django 2.2.3 on 2019-07-28 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitteraccounts', '0007_auto_20190728_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twitteraccount',
            name='chainid',
        ),
    ]
