# Generated by Django 2.2.28 on 2024-03-03 11:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamefolio_app', '0002_auto_20240301_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='datePosted',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 3, 11, 32, 1, 932238)),
        ),
    ]
