# Generated by Django 2.2.10 on 2022-03-21 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spwift', '0004_auto_20220321_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specifyuser',
            name='token',
        ),
        migrations.AddField(
            model_name='session',
            name='csfrtoken',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='sessionid',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]