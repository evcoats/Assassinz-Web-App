# Generated by Django 3.0.6 on 2020-06-16 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0013_auto_20200615_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='contactInfo',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='email',
            field=models.BooleanField(default=True),
        ),
    ]
