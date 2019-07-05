# Generated by Django 2.2.1 on 2019-07-05 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gerencial', '0014_productoconsignahistorico_productopotencialhistorico_productoretornohistorico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bitacora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=40)),
                ('accion', models.CharField(max_length=40)),
                ('fecha', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='productopotencialhistorico',
            name='nombre',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='productoretorno',
            name='codigo',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='productoretorno',
            name='idCliente',
            field=models.ForeignKey(db_column='idCliente', null=True, on_delete=django.db.models.deletion.CASCADE, to='gerencial.Cliente'),
        ),
        migrations.AlterField(
            model_name='productoretorno',
            name='idProveedor',
            field=models.ForeignKey(db_column='idProveedor', on_delete=django.db.models.deletion.CASCADE, to='gerencial.Proveedor'),
        ),
        migrations.AlterField(
            model_name='productoretorno',
            name='nombre_cliente',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='productoretorno',
            name='nombre_producto',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='productoretornohistorico',
            name='codigo',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='productoretornohistorico',
            name='idCliente',
            field=models.IntegerField(db_column='idCliente', null=True),
        ),
        migrations.AlterField(
            model_name='productoretornohistorico',
            name='nombre_cliente',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='productoretornohistorico',
            name='nombre_producto',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
