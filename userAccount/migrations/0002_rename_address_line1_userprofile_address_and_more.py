# Generated by Django 4.1 on 2022-10-23 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='address_line1',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='address_line2',
        ),
    ]
