# Generated by Django 4.0.6 on 2022-08-03 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0030_rename_images_tag_slike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slike',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todos.tagimage'),
        ),
    ]
