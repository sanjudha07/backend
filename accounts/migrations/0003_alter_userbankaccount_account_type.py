# Generated by Django 4.1.7 on 2023-02-16 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_userbankaccount_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbankaccount',
            name='account_type',
            field=models.CharField(max_length=20),
        ),
    ]
