# Generated by Django 5.1.3 on 2024-11-18 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_movie_franchise_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
    ]