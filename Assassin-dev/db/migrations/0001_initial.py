# Generated by Django 3.0.6 on 2020-06-10 16:55

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WitnessProtection', models.BooleanField()),
                ('Saftey', models.BooleanField()),
                ('SafteyZones', models.CharField(max_length=500)),
                ('KillMethod', models.CharField(max_length=500)),
                ('ExtraRules', models.CharField(max_length=500)),
                ('TimeCreated', models.DateTimeField(verbose_name='time')),
                ('TimeStart', models.DateTimeField(verbose_name='time')),
                ('TimeEnd', models.DateTimeField(verbose_name='time')),
            ],
        ),
        migrations.CreateModel(
            name='Kill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('killerID', models.IntegerField(default=0)),
                ('killedID', models.IntegerField(default=0)),
                ('gameID', models.IntegerField(default=0)),
                ('timeKilled', models.DateTimeField(verbose_name='time killed')),
            ],
        ),
        migrations.CreateModel(
            name='Mod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameID', models.IntegerField(default=0)),
                ('userID', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.IntegerField(default=0)),
                ('gameID', models.IntegerField(default=0)),
                ('kills', models.IntegerField(default=0)),
                ('targetID', models.IntegerField(default=0)),
                ('alive', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('KD', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20)),
                ('games', models.IntegerField(default=0)),
                ('wins', models.IntegerField(default=0)),
                ('mods', models.IntegerField(default=0)),
            ],
        ),
    ]