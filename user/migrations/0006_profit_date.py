# Generated by Django 5.2.3 on 2025-06-24 17:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_profit'),
    ]

    operations = [
        migrations.AddField(
            model_name='profit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 24, 18, 49, 13, 567980)),
        ),
    ]
