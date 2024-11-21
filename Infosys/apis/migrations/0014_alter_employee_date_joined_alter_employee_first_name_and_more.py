# Generated by Django 5.1.3 on 2024-11-20 17:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apis", "0013_alter_employee_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="date_joined",
            field=models.DateField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name="employee",
            name="first_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="employee",
            name="hourly_rate",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0.0, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="last_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="employee",
            name="status",
            field=models.CharField(
                blank=True, default="Active", max_length=100, null=True
            ),
        ),
    ]
