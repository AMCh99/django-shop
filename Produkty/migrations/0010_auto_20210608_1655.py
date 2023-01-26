# Generated by Django 3.2.3 on 2021-06-08 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0009_koszyk_profil'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='koszyk',
            options={'verbose_name': 'Koszyk', 'verbose_name_plural': 'Koszyki'},
        ),
        migrations.AlterModelOptions(
            name='profil',
            options={'verbose_name': 'Profil', 'verbose_name_plural': 'Profile'},
        ),
        migrations.AddField(
            model_name='koszyk',
            name='kosz_profil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Produkty.profil'),
        ),
        migrations.AddField(
            model_name='koszyk',
            name='produkt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Produkty.produkty'),
        ),
    ]