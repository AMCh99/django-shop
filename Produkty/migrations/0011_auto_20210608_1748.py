# Generated by Django 3.2.3 on 2021-06-08 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0010_auto_20210608_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='koszyk',
            name='produkt',
        ),
        migrations.CreateModel(
            name='Koszyk_Przedmioty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilosc', models.IntegerField(default=1)),
                ('cena_razem', models.FloatField(blank=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produkty.koszyk')),
                ('przedmiot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produkty.produkty')),
            ],
        ),
    ]