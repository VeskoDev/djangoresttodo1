# Generated by Django 4.0.6 on 2022-08-04 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0037_remove_prikazslika_slike_prikazslika_slike'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prikazslika',
            name='slike',
        ),
        migrations.RemoveField(
            model_name='slike',
            name='slikaJedna',
        ),
        migrations.AddField(
            model_name='prikazslika',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='todos.slike'),
        ),
        migrations.AddField(
            model_name='prikazslika',
            name='slika',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]