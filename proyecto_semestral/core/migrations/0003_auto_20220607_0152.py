# Generated by Django 3.1 on 2022-06-07 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220606_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(max_length=100, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='sustrato',
            name='tipoSustrato',
            field=models.CharField(max_length=50, verbose_name='Tipo de Sustra'),
        ),
    ]
