# Generated by Django 5.0 on 2024-11-17 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0074_modulo_company_alter_modulo_icon_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modulo',
            name='icon',
        ),
        migrations.AddField(
            model_name='modulo',
            name='Icon',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]