# Generated by Django 3.1.2 on 2021-01-04 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeDB', '0002_auto_20210104_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedb',
            name='eMobNo',
            field=models.PositiveBigIntegerField(),
        ),
    ]
