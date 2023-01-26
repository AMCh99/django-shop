# Generated by Django 3.2.3 on 2021-06-05 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwaproducenta', models.CharField(max_length=50)),
                ('opisproducenta', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='produkty',
            options={'verbose_name': 'Produkt', 'verbose_name_plural': 'Produkty'},
        ),
        migrations.AlterField(
            model_name='produkty',
            name='cena',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='produkty',
            name='nazwa',
            field=models.CharField(max_length=50),
        ),
    ]
