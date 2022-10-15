# Generated by Django 4.0.6 on 2022-10-15 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_alter_payment_amtapply'),
    ]

    operations = [
        migrations.CreateModel(
            name='cust_statment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(default='', max_length=255)),
                ('Date', models.DateField()),
                ('Transactions', models.CharField(default='', max_length=255)),
                ('Details', models.CharField(default='', max_length=255)),
                ('Amount', models.FloatField()),
                ('Payments', models.FloatField()),
                ('Balance', models.FloatField()),
                ('invoice', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app1.invoice')),
                ('payment', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app1.payment')),
            ],
        ),
    ]