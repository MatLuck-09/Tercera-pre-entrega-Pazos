# Generated by Django 4.1.5 on 2023-06-21 20:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('battles', '0006_ejercito1_ejercito2_batalla_resultado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='batalla',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='batalla',
            name='imagen',
            field=models.ImageField(default='C:/Users/Nicol/Desktop/Proyectos Django/Proyecto-6/HistoryBattles/media/battles', upload_to=''),
        ),
        migrations.AddField(
            model_name='batalla',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='ejercito1',
            name='asedio',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ejercito1',
            name='caballeria',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ejercito1',
            name='criaturas',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ejercito1',
            name='infanteria',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ejercito1',
            name='mercenarios',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ejercito1',
            name='proyectiles',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ejercito1',
            name='tropas_elite',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ejercito2',
            name='asedio',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ejercito2',
            name='caballeria',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ejercito2',
            name='criaturas',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ejercito2',
            name='infanteria',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ejercito2',
            name='mercenarios',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ejercito2',
            name='proyectiles',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ejercito2',
            name='tropas_elite',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
