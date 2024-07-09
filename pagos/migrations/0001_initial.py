# Generated by Django 5.0.6 on 2024-07-09 21:33

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ventas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalPago',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('id_pago', models.CharField(db_index=True, max_length=6)),
                ('created_by', models.EmailField(max_length=254)),
                ('creation_date', models.DateTimeField(blank=True, editable=False)),
                ('tienda', models.CharField(choices=[('Madrid', 'Madrid'), ('Barcelona', 'Barcelona'), ('Valencia', 'Valencia'), ('Videollamada', 'Videollamada')], max_length=20)),
                ('metodo_de_pago', models.CharField(choices=[('Efectivo', 'Efectivo'), ('Tarjeta', 'Tarjeta'), ('BBVA', 'BBVA'), ('SumUp', 'SumUp'), ('Bizum', 'Bizum'), ('Transferencia', 'Transferencia'), ('Paypal', 'Paypal'), ('Web', 'Web')], max_length=20)),
                ('importe', models.DecimalField(decimal_places=2, max_digits=10)),
                ('n_f_simplificada', models.CharField(blank=True, max_length=255, null=True)),
                ('productos_comprados', models.TextField(blank=True, null=True)),
                ('detalles_del_ticket', models.TextField(blank=True, null=True)),
                ('lista_de_productos', models.TextField(blank=True, null=True)),
                ('duplicados', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('id_ventas', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ventas.venta')),
            ],
            options={
                'verbose_name': 'historical pago',
                'verbose_name_plural': 'historical pagos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pago', models.CharField(max_length=6, unique=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('tienda', models.CharField(choices=[('Madrid', 'Madrid'), ('Barcelona', 'Barcelona'), ('Valencia', 'Valencia'), ('Videollamada', 'Videollamada')], max_length=20)),
                ('metodo_de_pago', models.CharField(choices=[('Efectivo', 'Efectivo'), ('Tarjeta', 'Tarjeta'), ('BBVA', 'BBVA'), ('SumUp', 'SumUp'), ('Bizum', 'Bizum'), ('Transferencia', 'Transferencia'), ('Paypal', 'Paypal'), ('Web', 'Web')], max_length=20)),
                ('importe', models.DecimalField(decimal_places=2, max_digits=10)),
                ('n_f_simplificada', models.CharField(blank=True, max_length=255, null=True)),
                ('productos_comprados', models.TextField(blank=True, null=True)),
                ('detalles_del_ticket', models.TextField(blank=True, null=True)),
                ('lista_de_productos', models.TextField(blank=True, null=True)),
                ('duplicados', models.BooleanField(default=False)),
                ('id_ventas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagos', to='ventas.venta')),
            ],
        ),
    ]