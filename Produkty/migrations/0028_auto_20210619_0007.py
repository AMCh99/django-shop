# Generated by Django 3.2.3 on 2021-06-18 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0027_alter_historia_zakupów_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producent',
            name='opis_producenta',
        ),
        migrations.RemoveField(
            model_name='produkty',
            name='zdjęcie',
        ),
    ]
