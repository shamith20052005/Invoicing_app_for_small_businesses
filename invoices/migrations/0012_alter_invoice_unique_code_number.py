# Generated by Django 4.1.5 on 2023-05-15 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0011_invoice_unique_code_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='unique_code_number',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
