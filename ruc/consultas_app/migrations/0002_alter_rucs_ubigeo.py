# Generated by Django 4.2 on 2023-04-18 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rucs',
            name='ubigeo',
            field=models.CharField(max_length=6),
        ),
    ]