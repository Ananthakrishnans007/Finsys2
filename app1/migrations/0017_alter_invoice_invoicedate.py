# Generated by Django 4.0.6 on 2022-10-13 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_alter_payment_amtcredit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoicedate',
            field=models.DateField(),
        ),
    ]