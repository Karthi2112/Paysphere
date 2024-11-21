# Generated by Django 5.1.3 on 2024-11-14 15:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apis", "0002_customuser_phone_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employee",
            name="address",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="employment_history",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="status",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="user",
        ),
        migrations.AddField(
            model_name="employee",
            name="role",
            field=models.CharField(default="Employee", max_length=100),
        ),
        migrations.AlterField(
            model_name="employee",
            name="date_joined",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="employee",
            name="phone",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]