# Generated by Django 4.0.6 on 2022-10-14 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0023_alter_payment_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='balance',
            field=models.FloatField(default='0'),
        ),
    ]