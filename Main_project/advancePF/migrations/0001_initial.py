# Generated by Django 5.1.4 on 2024-12-11 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvanceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('invoice_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_words', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('purpose', models.TextField()),
                ('account_user', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProcurementRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VendorQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.DecimalField(decimal_places=2, max_digits=10)),
                ('procurement_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advancePF.procurementrequest')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advancePF.vendor')),
            ],
        ),
        migrations.AddField(
            model_name='procurementrequest',
            name='vendors',
            field=models.ManyToManyField(through='advancePF.VendorQuote', to='advancePF.vendor'),
        ),
    ]
