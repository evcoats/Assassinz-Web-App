# Generated by Django 3.1.6 on 2021-03-07 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0020_auto_20200831_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fullName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
