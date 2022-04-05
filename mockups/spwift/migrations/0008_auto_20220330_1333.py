# Generated by Django 3.2.12 on 2022-03-30 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spwift', '0007_preparationtype_sppreptypeid'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spid', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='collobjectrecord',
            name='spid',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='preparationtype',
            name='spid',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='spcollection',
            name='spid',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='specifyuser',
            name='spid',
            field=models.IntegerField(null=True),
        ),
    ]
