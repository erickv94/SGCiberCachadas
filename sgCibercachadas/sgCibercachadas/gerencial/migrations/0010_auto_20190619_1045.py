# Generated by Django 2.2.1 on 2019-06-19 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gerencial', '0009_detalleventa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleventa',
            name='idVenta',
            field=models.ForeignKey(db_column='idVenta', null=True, on_delete=django.db.models.deletion.CASCADE, to='gerencial.Venta'),
        ),
    ]
