# Generated by Django 4.0.6 on 2022-08-02 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0018_title_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programmer',
            name='language',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='Paradigm',
        ),
        migrations.DeleteModel(
            name='Programmer',
        ),
    ]
