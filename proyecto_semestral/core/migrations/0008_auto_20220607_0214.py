# Generated by Django 3.1 on 2022-06-07 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20220607_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='macetero',
            name='precioMacetero',
            field=models.IntegerField(default=0, verbose_name='Precio de Macetero'),
        ),
        migrations.AddField(
            model_name='macetero',
            name='stockMacetero',
            field=models.IntegerField(default=0, verbose_name='Stock de Macetero'),
        ),
    ]
