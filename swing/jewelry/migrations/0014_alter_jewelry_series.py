# Generated by Django 4.2.13 on 2024-06-25 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0013_remove_jewelry_serious_jewelry_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jewelry',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jewelry.series', verbose_name='Series'),
        ),
    ]
