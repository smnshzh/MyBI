# Generated by Django 3.2.15 on 2022-12-24 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicData', '0002_auto_20221223_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostumersActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=225)),
            ],
            options={
                'verbose_name': 'فعالیت مشتری',
                'verbose_name_plural': 'فعالیتها',
            },
        ),
        migrations.CreateModel(
            name='Dc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=225)),
                ('activation', models.BooleanField(default=False)),
                ('ggroups', models.ManyToManyField(related_name='GoodsCanSAle', to='basicData.GoodsMainGroup')),
            ],
            options={
                'verbose_name': 'مرکز اصلی',
                'verbose_name_plural': 'مراکز اصلی',
            },
        ),
        migrations.CreateModel(
            name='Superviseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=225)),
                ('activation', models.BooleanField(default=False)),
                ('MainDc', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basicData.dc')),
            ],
            options={
                'verbose_name': 'سرپرست',
                'verbose_name_plural': 'سرپرستان',
            },
        ),
        migrations.CreateModel(
            name='SaleLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=225)),
                ('divideGroup', models.ManyToManyField(to='basicData.GoodsDivideGroup')),
            ],
            options={
                'verbose_name': 'لاین فروش',
                'verbose_name_plural': 'لاین های فروش',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=225)),
                ('activation', models.BooleanField(default=False)),
                ('position', models.CharField(choices=[(1, 'مدیر'), (2, 'رئیس')], max_length=4)),
                ('MainDc', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basicData.dc')),
            ],
            options={
                'verbose_name': 'مدیر شعبه',
                'verbose_name_plural': 'مدیریت شعب',
            },
        ),
        migrations.CreateModel(
            name='DistrictManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=225)),
                ('activation', models.BooleanField(default=False)),
                ('MainDcs', models.ManyToManyField(related_name='MainDC', to='basicData.Dc')),
            ],
            options={
                'verbose_name': 'مدیر منطقه',
                'verbose_name_plural': 'مدیران مناطق',
            },
        ),
        migrations.CreateModel(
            name='Barache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=225)),
                ('activation', models.BooleanField(default=False)),
                ('mainDc', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basicData.dc')),
            ],
            options={
                'verbose_name': 'مرکز فروش',
                'verbose_name_plural': 'مراکز فروش',
            },
        ),
    ]