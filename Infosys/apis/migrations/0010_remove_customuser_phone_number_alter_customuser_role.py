# Generated by Django 5.1.3 on 2024-11-18 16:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apis", "0009_alter_customuser_role"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="phone_number",
        ),
        migrations.AlterField(
            model_name="customuser",
            name="role",
            field=models.CharField(
                choices=[
                    ("HR", "HR"),
                    ("Manager", "Manager"),
                    ("Software Engineer", "Software Engineer"),
                    ("Developer", "Developer"),
                ],
                default="Developer",
                max_length=50,
            ),
        ),
    ]
