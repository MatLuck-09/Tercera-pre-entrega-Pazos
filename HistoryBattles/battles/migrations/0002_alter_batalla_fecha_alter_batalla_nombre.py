# Generated by Django 4.1.5 on 2023-06-21 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batalla',
            name='fecha',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='batalla',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
