# Generated by Django 2.1.3 on 2018-11-13 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='slug',
            field=models.SlugField(blank=True, max_length=60, unique=True, verbose_name='slug'),
        ),
    ]
