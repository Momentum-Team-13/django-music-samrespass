# Generated by Django 4.0.5 on 2022-07-01 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djamming', '0006_remove_album_tracks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='track',
            new_name='song',
        ),
    ]
