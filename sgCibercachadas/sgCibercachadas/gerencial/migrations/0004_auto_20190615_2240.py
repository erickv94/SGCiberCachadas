# Generated by Django 2.2.1 on 2019-06-16 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gerencial', '0003_auto_20190613_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='idEmpleado',
        ),
        migrations.DeleteModel(
            name='Empleado',
        ),
    ]
