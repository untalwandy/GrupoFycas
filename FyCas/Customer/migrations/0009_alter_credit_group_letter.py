# Generated by Django 5.0 on 2024-12-05 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0008_credit_group_letter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='group_letter',
            field=models.CharField(default='A', max_length=1),
        ),
    ]