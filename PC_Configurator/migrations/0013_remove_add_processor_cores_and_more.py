# Generated by Django 4.1.7 on 2023-03-19 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PC_Configurator', '0012_add_processor_cores_add_processor_frequency_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_processor',
            name='Cores',
        ),
        migrations.RemoveField(
            model_name='add_processor',
            name='Frequency',
        ),
        migrations.RemoveField(
            model_name='add_processor',
            name='Graphics_core',
        ),
        migrations.RemoveField(
            model_name='add_processor',
            name='Heat_dissipation',
        ),
        migrations.RemoveField(
            model_name='add_processor',
            name='Max_RAM_frequency',
        ),
    ]
