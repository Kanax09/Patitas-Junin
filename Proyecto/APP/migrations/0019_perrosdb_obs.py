# Generated by Django 5.0.6 on 2024-06-21 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0018_alter_vacunas_perrodb_vac1'),
    ]

    operations = [
        migrations.AddField(
            model_name='perrosdb',
            name='obs',
            field=models.TextField(default=None, max_length=500, verbose_name='Observaciones'),
        ),
    ]
