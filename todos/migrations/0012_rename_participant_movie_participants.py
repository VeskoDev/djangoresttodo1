# Generated by Django 4.0.6 on 2022-08-01 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0011_remove_participant_title_participant_titles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='participant',
            new_name='participants',
        ),
    ]
