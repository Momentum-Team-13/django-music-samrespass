# Generated by Django 4.0.5 on 2022-06-30 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djamming', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_art',
            field=models.ImageField(upload_to='static/images/album_art/'),
        ),
    ]