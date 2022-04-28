# Generated by Django 3.2.12 on 2022-04-07 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spwift', '0014_auto_20220407_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='spuser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='spwift.specifyuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datasetrow',
            name='dataset',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='spwift.dataset'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preparationtype',
            name='collection',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='spwift.spcollection'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='currentcollection',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='spwift.spcollection'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='currentpreptype',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='spwift.preparationtype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='spuser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='spwift.specifyuser'),
            preserve_default=False,
        ),
    ]
