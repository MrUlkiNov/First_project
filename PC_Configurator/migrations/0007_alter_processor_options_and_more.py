# Generated by Django 4.1.7 on 2023-03-17 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PC_Configurator', '0006_alter_processor_options_alter_processor_cores_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='processor',
            options={'ordering': ('Name',), 'verbose_name': 'Процессор', 'verbose_name_plural': 'Процессоры'},
        ),
        migrations.AlterField(
            model_name='processor',
            name='Graphics_core',
            field=models.CharField(blank=True, default='Не имеется', max_length=40, verbose_name='Графическое ядро'),
        ),
    ]