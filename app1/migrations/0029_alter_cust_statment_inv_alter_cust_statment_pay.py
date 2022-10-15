# Generated by Django 4.0.6 on 2022-10-15 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0028_alter_cust_statment_inv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cust_statment',
            name='inv',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='app1.invoice'),
        ),
        migrations.AlterField(
            model_name='cust_statment',
            name='pay',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='app1.payment'),
        ),
    ]