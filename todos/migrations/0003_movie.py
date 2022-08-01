# Generated by Django 4.0.6 on 2022-07-31 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_todo_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]