# Generated by Django 3.2.15 on 2022-12-25 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicData', '0004_auto_20221225_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='saler',
            name='superviseur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='basicData.superviseur'),
            preserve_default=False,
        ),
    ]