# Generated by Django 3.2.13 on 2022-06-29 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_alter_rainfall_raingauge_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rainfall',
            name='raingauge_code',
            field=models.IntegerField(),
        ),
    ]
