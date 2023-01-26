# Generated by Django 3.2.3 on 2021-06-08 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Produkty', '0016_auto_20210608_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='koszyk',
            name='kosz_profil',
        ),
        migrations.AddField(
            model_name='koszyk',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]