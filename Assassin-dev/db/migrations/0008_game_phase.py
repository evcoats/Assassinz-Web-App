# Generated by Django 3.0.6 on 2020-06-12 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_user_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='phase',
            field=models.IntegerField(default=0),
        ),
    ]
