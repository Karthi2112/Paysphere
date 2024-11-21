# Generated by Django 5.1.3 on 2024-11-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apis", "0006_employee_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employee",
            name="department",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="salary",
        ),
        migrations.AlterField(
            model_name="employee",
            name="date_joined",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="employee",
            name="hourly_rate",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="phone",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name="employee",
            name="role",
            field=models.CharField(
                choices=[
                    ("Software Engineer", "Software Engineer"),
                    ("Manager", "Manager"),
                    ("Hr", "HR"),
                    ("Developer", "Developer"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="status",
            field=models.CharField(
                choices=[("Active", "Active"), ("Inactive", "Inactive")], max_length=50
            ),
        ),
    ]