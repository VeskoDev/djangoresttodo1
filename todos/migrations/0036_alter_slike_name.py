# Generated by Django 4.0.6 on 2022-08-04 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0035_prikazslika_slike_delete_tag12_delete_tagimage12_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slike',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]