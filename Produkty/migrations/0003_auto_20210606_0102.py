# Generated by Django 3.2.3 on 2021-06-05 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0002_auto_20210606_0101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producent',
            options={'verbose_name': 'Producent', 'verbose_name_plural': 'Producenci'},
        ),
        migrations.RenameField(
            model_name='producent',
            old_name='nazwaproducenta',
            new_name='nazwa_producenta',
        ),
        migrations.RenameField(
            model_name='producent',
            old_name='opisproducenta',
            new_name='opis_producenta',
        ),
    ]