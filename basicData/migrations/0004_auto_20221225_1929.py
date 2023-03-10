# Generated by Django 3.2.15 on 2022-12-25 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicData', '0003_barache_costumersactivity_dc_districtmanager_manager_saleline_superviseur'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='barache',
            options={'verbose_name': '6-مرکز فروش', 'verbose_name_plural': '6-مراکز فروش'},
        ),
        migrations.AlterModelOptions(
            name='costumersactivity',
            options={'verbose_name': '11-فعالیت مشتری', 'verbose_name_plural': '11-فعالیتها'},
        ),
        migrations.AlterModelOptions(
            name='dc',
            options={'verbose_name': '5-مرکز اصلی', 'verbose_name_plural': '5-مراکز اصلی'},
        ),
        migrations.AlterModelOptions(
            name='districtmanager',
            options={'verbose_name': '7-مدیر منطقه', 'verbose_name_plural': '7-مدیران مناطق'},
        ),
        migrations.AlterModelOptions(
            name='manager',
            options={'verbose_name': '8-مدیر شعبه', 'verbose_name_plural': '8-مدیریت شعب'},
        ),
        migrations.AlterModelOptions(
            name='saleline',
            options={'verbose_name': '10-لاین فروش', 'verbose_name_plural': '10-لاین های فروش'},
        ),
        migrations.AlterModelOptions(
            name='superviseur',
            options={'verbose_name': '9-سرپرست', 'verbose_name_plural': '9-سرپرستان'},
        ),
        migrations.CreateModel(
            name='SalerActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=225)),
                ('costumerActivity', models.ManyToManyField(to='basicData.CostumersActivity')),
            ],
            options={
                'verbose_name': 'فعالیت فروشنده',
                'verbose_name_plural': 'فعالیت فروشندگان',
            },
        ),
        migrations.CreateModel(
            name='Saler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scode', models.IntegerField()),
                ('pcode', models.IntegerField()),
                ('name', models.CharField(max_length=225)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basicData.barache')),
            ],
            options={
                'verbose_name': 'فروشنده',
                'verbose_name_plural': 'فروشندگان',
            },
        ),
    ]
