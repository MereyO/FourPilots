# Generated by Django 4.0.4 on 2022-05-01 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], null=True),
        ),
    ]
