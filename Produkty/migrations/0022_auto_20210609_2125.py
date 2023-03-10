# Generated by Django 3.2.3 on 2021-06-09 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Produkty', '0021_alter_produkty_cena'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='koszyk_przedmioty',
            options={'verbose_name': 'Przedmioty w Koszyku', 'verbose_name_plural': 'Przedmioty w Koszykach'},
        ),
        migrations.CreateModel(
            name='Historia_zakupów',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilosc', models.IntegerField(default=1)),
                ('data_zakupu', models.DateField(auto_now_add=True)),
                ('przedmiot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produkty.produkty')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Historia_zakupów',
                'verbose_name_plural': 'Historia_zakupów',
            },
        ),
    ]
