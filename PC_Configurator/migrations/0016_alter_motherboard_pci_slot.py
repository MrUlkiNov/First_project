# Generated by Django 4.1.7 on 2023-03-19 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PC_Configurator', '0015_motherboard_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motherboard',
            name='PCI_slot',
            field=models.CharField(default='PCI-Ex16', max_length=10, verbose_name='Слоты PCI'),
        ),
    ]