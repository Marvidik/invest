# Generated by Django 5.2.3 on 2025-06-25 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_withdrawal_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kyc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='kyc',
            field=models.BooleanField(default=False),
        ),
    ]
