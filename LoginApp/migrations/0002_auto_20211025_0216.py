# Generated by Django 2.2.19 on 2021-10-25 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='c_postal',
            field=models.CharField(max_length=6, verbose_name='Codigo Postal'),
        ),
    ]