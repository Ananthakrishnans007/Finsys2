# Generated by Django 4.0.6 on 2022-10-21 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0044_alter_customer_receivables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='file',
            field=models.FileField(default='default.jpg', upload_to='Customer'),
        ),
    ]
