# Generated by Django 4.1.7 on 2023-03-19 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PC_Configurator', '0020_remove_add_videocard_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videocard',
            name='Name',
            field=models.CharField(max_length=100, verbose_name='Наименоваие'),
        ),
    ]
