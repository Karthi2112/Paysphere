# Generated by Django 5.1.3 on 2024-12-05 16:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apis", "0023_remove_payroll_scheduled_date_payroll_status_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="salary",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]