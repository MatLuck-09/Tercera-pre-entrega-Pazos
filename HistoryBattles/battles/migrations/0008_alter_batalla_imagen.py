# Generated by Django 4.1.5 on 2023-06-21 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battles', '0007_batalla_created_batalla_imagen_batalla_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batalla',
            name='imagen',
            field=models.ImageField(upload_to='battles'),
        ),
    ]
