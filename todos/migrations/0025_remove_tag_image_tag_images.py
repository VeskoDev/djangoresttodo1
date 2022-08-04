# Generated by Django 4.0.6 on 2022-08-03 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0024_remove_tag_images_tag_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='image',
        ),
        migrations.AddField(
            model_name='tag',
            name='images',
            field=models.ManyToManyField(related_name='tags', to='todos.tagimage'),
        ),
    ]
