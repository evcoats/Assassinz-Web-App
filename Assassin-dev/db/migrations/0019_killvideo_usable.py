# Generated by Django 3.0.6 on 2020-07-04 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0018_killvideo_killconf'),
    ]

    operations = [
        migrations.AddField(
            model_name='killvideo',
            name='usable',
            field=models.BooleanField(default=True),
        ),
    ]
