# Generated by Django 5.0 on 2024-10-07 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0058_cuota_restante'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='estado',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
