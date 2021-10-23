# Generated by Django 2.2.19 on 2021-10-22 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30, unique=True, verbose_name='Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duracion', models.DurationField(verbose_name='Duracion')),
            ],
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalles', models.CharField(max_length=20, unique=True, verbose_name='Detalles')),
                ('simbolo', models.CharField(max_length=2, verbose_name='simbolo')),
            ],
        ),
        migrations.CreateModel(
            name='Recordatorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo', models.DurationField(verbose_name='Tiempo')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, unique=True, verbose_name='Nombre')),
                ('telefono', models.CharField(max_length=8, unique=True, verbose_name='Telefono')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebPayments.Categoria')),
                ('ciclo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebPayments.Ciclo')),
                ('moneda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebPayments.Moneda', verbose_name='Moneda')),
                ('recordatorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebPayments.Recordatorio')),
            ],
        ),
    ]
