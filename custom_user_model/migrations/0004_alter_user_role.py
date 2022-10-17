# Generated by Django 4.1 on 2022-10-16 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user_model', '0003_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Vendor'), (2, 'Customer')], null=True),
        ),
    ]
