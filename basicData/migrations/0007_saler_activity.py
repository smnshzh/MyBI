# Generated by Django 3.2.15 on 2022-12-25 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicData', '0006_alter_superviseur_maindc'),
    ]

    operations = [
        migrations.AddField(
            model_name='saler',
            name='activity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='basicData.saleractivity'),
            preserve_default=False,
        ),
    ]