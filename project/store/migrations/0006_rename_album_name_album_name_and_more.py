# Generated by Django 5.1.3 on 2024-11-20 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_franchise_name_movie_franchise_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='artist_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='franchise',
            old_name='franchise_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='movie_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='song_name',
            new_name='name',
        ),
    ]
