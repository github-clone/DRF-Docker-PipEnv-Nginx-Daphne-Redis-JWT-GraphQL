# Generated by Django 2.1.2 on 2018-10-23 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0003_adding_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basicinformation',
            options={'verbose_name': 'user profile', 'verbose_name_plural': 'user profiles'},
        ),
    ]
