# Generated by Django 4.2.13 on 2024-06-21 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
        ('jewelry', '0004_alter_linkjewelryjewelrystring_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bead',
            name='purchase_link',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Purchase Link'),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='purchase_link',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Purchase Link'),
        ),
        migrations.AlterField(
            model_name='jewelrystring',
            name='purchase_link',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Purchase Link'),
        ),
        migrations.CreateModel(
            name='LinkJewelryPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('jewelry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jewelry.jewelry')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='package.package', verbose_name='Package')),
            ],
            options={
                'verbose_name': 'Package',
                'verbose_name_plural': 'Packages',
            },
        ),
        migrations.AddField(
            model_name='jewelry',
            name='packages',
            field=models.ManyToManyField(through='jewelry.LinkJewelryPackage', to='package.package'),
        ),
    ]
