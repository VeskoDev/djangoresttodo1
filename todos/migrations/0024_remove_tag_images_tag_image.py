# Generated by Django 4.0.6 on 2022-08-03 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0023_remove_tagimage_tag_tag_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='images',
        ),
        migrations.AddField(
            model_name='tag',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]