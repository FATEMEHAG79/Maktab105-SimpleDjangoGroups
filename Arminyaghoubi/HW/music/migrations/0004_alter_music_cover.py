# Generated by Django 5.0.2 on 2024-02-12 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_music_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='cover',
            field=models.ImageField(upload_to='media/'),
        ),
    ]