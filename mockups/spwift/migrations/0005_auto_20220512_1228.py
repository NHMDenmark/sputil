# Generated by Django 2.2.10 on 2022-05-12 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spwift', '0004_auto_20220511_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasetrow',
            name='highertaxonid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datasetrow',
            name='preptypeid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
