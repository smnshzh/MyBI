# Generated by Django 3.2.15 on 2022-12-25 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicData', '0005_saler_superviseur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superviseur',
            name='MainDc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basicData.barache'),
        ),
    ]
