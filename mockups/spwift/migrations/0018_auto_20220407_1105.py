# Generated by Django 3.2.12 on 2022-04-07 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spwift', '0017_auto_20220407_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasetrow',
            name='highertaxon',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='datasetrow',
            name='preptype',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]