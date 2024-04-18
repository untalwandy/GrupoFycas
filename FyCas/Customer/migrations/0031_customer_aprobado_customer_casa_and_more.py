# Generated by Django 5.0 on 2024-04-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0030_customer_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='aprobado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='casa',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='familiar_en_fycas',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='fue_recomendado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='tierra',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='vehiculo',
            field=models.BooleanField(default=False),
        ),
    ]
