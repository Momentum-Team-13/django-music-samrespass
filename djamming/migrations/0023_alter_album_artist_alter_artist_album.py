# Generated by Django 4.0.5 on 2022-07-07 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djamming', '0022_alter_album_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artist', to='djamming.artist'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album', to='djamming.album'),
        ),
    ]
