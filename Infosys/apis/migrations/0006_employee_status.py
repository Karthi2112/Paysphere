# Generated by Django 5.1.3 on 2024-11-15 14:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apis", "0005_employee_hourly_rate"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="status",
            field=models.CharField(default="Active", max_length=100),
        ),
    ]
