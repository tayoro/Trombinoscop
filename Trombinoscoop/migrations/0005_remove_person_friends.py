# Generated by Django 3.2.5 on 2022-03-06 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trombinoscoop', '0004_alter_person_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='friends',
        ),
    ]