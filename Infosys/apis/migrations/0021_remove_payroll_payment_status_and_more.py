# Generated by Django 5.1.3 on 2024-12-02 16:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apis", "0020_scheduledpayment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payroll",
            name="payment_status",
        ),
        migrations.RemoveField(
            model_name="payroll",
            name="processed_date",
        ),
        migrations.AddField(
            model_name="payroll",
            name="payment_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="payroll",
            name="scheduled_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
