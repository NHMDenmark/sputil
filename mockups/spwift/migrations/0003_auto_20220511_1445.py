# Generated by Django 2.2.10 on 2022-05-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spwift', '0002_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='BroadGeographicRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spid', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.AlterField(
            model_name='collection',
            name='spid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='public',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='spid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datasetrow',
            name='datetimecreated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datasetrow',
            name='datetimemodified',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datasetrow',
            name='spid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='spid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='highertaxon',
            name='spid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='preparationtype',
            name='spid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='specifyuser',
            name='spid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
