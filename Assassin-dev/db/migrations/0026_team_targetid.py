# Generated by Django 4.0 on 2021-12-28 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0025_game_randomteams'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='targetID',
            field=models.IntegerField(default=0),
        ),
    ]
