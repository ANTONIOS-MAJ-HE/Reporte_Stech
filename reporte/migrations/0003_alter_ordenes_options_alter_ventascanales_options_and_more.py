# Generated by Django 5.0.4 on 2024-04-08 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporte', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordenes',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='ventascanales',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='ventasdiarias',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='ventasproductos',
            options={'managed': False},
        ),
    ]
