# Generated by Django 5.1.3 on 2024-11-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apis", "0012_employee_created_at_employee_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="role",
            field=models.CharField(
                blank=True,
                choices=[
                    ("HR", "HR"),
                    ("Manager", "Manager"),
                    ("Software Engineer", "Software Engineer"),
                    ("Developer", "Developer"),
                ],
                default="Developer",
                max_length=100,
                null=True,
            ),
        ),
    ]