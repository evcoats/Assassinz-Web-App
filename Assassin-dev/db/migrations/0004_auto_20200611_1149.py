# Generated by Django 3.0.6 on 2020-06-11 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_auto_20200611_1144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='SafteyZones',
            new_name='SafetyZones',
        ),
    ]