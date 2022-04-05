# Generated by Django 2.2.10 on 2022-03-21 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spwift', '0003_auto_20220321_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollObjectRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spcollectionobjectid', models.BigIntegerField(blank=True, null=True)),
                ('barcode', models.CharField(blank=True, max_length=64, null=True)),
                ('catalogNumber', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PreparationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdatetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SpCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spcollectionid', models.BigIntegerField()),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='specifyuser',
            name='token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
