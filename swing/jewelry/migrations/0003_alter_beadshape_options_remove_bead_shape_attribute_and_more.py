# Generated by Django 4.2.13 on 2024-06-20 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0002_beadshapeattribute_bead_shape_attribute'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beadshape',
            options={'verbose_name': 'Bead Shape', 'verbose_name_plural': 'Bead Shapes'},
        ),
        migrations.RemoveField(
            model_name='bead',
            name='shape_attribute',
        ),
        migrations.CreateModel(
            name='LinkBeadBeadShapeAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bead', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jewelry.bead')),
                ('bead_shape_attribute', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jewelry.beadshapeattribute', verbose_name='Bead Shape Attribute')),
            ],
            options={
                'verbose_name': 'Bead Shape Attribute',
                'verbose_name_plural': 'Bead Shape Attributes',
                'unique_together': {('bead', 'bead_shape_attribute')},
            },
        ),
        migrations.AddField(
            model_name='bead',
            name='bead_shape_attributes',
            field=models.ManyToManyField(through='jewelry.LinkBeadBeadShapeAttribute', to='jewelry.beadshapeattribute'),
        ),
    ]
