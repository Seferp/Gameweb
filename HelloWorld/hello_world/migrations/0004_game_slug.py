# Generated by Django 4.1.7 on 2023-03-12 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0003_alter_game_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]