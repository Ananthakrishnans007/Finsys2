# Generated by Django 4.0.6 on 2022-10-21 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0042_alter_customer_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='file',
            field=models.FileField(null=True, upload_to='Customer'),
        ),
    ]