# Generated by Django 3.2.15 on 2022-12-26 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicData', '0009_auto_20221226_1905'),
        ('porsant', '0003_auto_20221226_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='salertargets',
            name='saler',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='basicData.saler'),
            preserve_default=False,
        ),
    ]
