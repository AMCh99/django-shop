# Generated by Django 3.2.3 on 2021-06-09 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0024_alter_historia_zakupów_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkty',
            name='zdjęcie',
            field=models.ImageField(blank=True, default=None, height_field=200, max_length=20, null=True, upload_to='uploads/', width_field=200),
        ),
    ]
