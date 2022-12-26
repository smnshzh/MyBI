# Generated by Django 3.2.15 on 2022-12-25 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicData', '0007_saler_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barache',
            name='code',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='costumersactivity',
            name='code',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='districtmanager',
            name='code',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='code',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='saleline',
            name='code',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='saler',
            name='scode',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='saleractivity',
            name='code',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='superviseur',
            name='code',
            field=models.IntegerField(unique=True),
        ),
    ]