# Generated by Django 4.0.5 on 2022-07-07 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djamming', '0020_alter_album_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.CharField(max_length=255, null=True),
        ),
    ]