# Generated by Django 5.0.6 on 2024-07-10 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_alter_historicalpedido_id_pedido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpedido',
            name='id_pedido',
            field=models.CharField(db_index=True, default='D667FC', max_length=6),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='id_pedido',
            field=models.CharField(default='D667FC', max_length=6, unique=True),
        ),
    ]
