# Generated by Django 5.0.6 on 2024-07-10 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_fiesta',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcliente',
            name='fecha_fiesta',
            field=models.DateField(blank=True, null=True),
        ),
    ]