# Generated by Django 4.0.4 on 2022-06-19 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flujoMigratorio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='paisOrigen',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='salida',
            name='paisDestino',
            field=models.CharField(default='', max_length=10),
        ),
    ]
