# Generated by Django 4.0.5 on 2022-07-07 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djamming', '0025_remove_artist_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='static/images/profile_pic/'),
        ),
    ]
