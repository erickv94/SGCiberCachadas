# Generated by Django 2.2.1 on 2019-06-12 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PermisosSoporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('semi_produ', 'Global customer rights'), ('vendor_rights', 'Global vendor rights'), ('any_rights', 'Global any rights')),
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaHora', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_promedio_compra', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=25)),
                ('idCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerencial.Categoria')),
                ('idInventario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerencial.Inventario')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoRetorno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('nombre_cliente', models.CharField(max_length=20)),
                ('nombre_producto', models.CharField(max_length=40)),
                ('codigo', models.CharField(max_length=10)),
                ('fecha', models.DateField()),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerencial.Cliente')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerencial.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoPotencial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('cantidad', models.IntegerField()),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerencial.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoConsigna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerencial.Cliente')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerencial.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Kardex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('precExistencia', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cantExistencias', models.IntegerField()),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerencial.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCompra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerencial.Compra')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerencial.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='idProveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerencial.Proveedor'),
        ),
    ]
