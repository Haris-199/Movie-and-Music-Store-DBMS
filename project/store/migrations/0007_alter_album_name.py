# Generated by Django 5.1.3 on 2024-11-20 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_album_name_album_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
