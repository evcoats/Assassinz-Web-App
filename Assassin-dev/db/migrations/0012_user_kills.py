# Generated by Django 3.0.6 on 2020-06-14 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0011_auto_20200613_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='kills',
            field=models.IntegerField(default=0),
        ),
    ]
