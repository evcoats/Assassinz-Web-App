# Generated by Django 4.0 on 2022-08-25 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0030_game_gamename_game_gamestring'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
