# Generated by Django 3.2.3 on 2021-06-08 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0015_auto_20210608_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='koszyk',
            name='user',
        ),
        migrations.AddField(
            model_name='koszyk',
            name='kosz_profil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Produkty.profil'),
        ),
    ]
