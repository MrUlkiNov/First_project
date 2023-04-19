# Generated by Django 4.1.7 on 2023-03-15 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PC_Configurator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='processor',
            name='Socket',
            field=models.CharField(choices=[('AM4', 'AM4'), ('AM3+', 'AM3+'), ('LGA 1151', 'LGA 1151'), ('LGA 1200', 'LGA 1200'), ('LGA 1700', 'LGA 1700')], default='LGA 1151', max_length=8),
        ),
        migrations.AlterField(
            model_name='processor',
            name='Memory_type',
            field=models.CharField(choices=[('DDR3', 'DDR3'), ('DDR4', 'DDR4'), ('DDR5', 'DDR5')], max_length=4),
        ),
    ]