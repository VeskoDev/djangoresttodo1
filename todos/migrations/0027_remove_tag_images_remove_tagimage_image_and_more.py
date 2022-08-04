# Generated by Django 4.0.6 on 2022-08-03 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0026_alter_tag_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='images',
        ),
        migrations.RemoveField(
            model_name='tagimage',
            name='image',
        ),
        migrations.AddField(
            model_name='tagimage',
            name='images',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='tagimage',
            name='tag',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='todos.tag'),
        ),
    ]