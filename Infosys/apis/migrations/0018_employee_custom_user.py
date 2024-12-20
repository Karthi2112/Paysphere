# Generated by Django 5.1.3 on 2024-11-29 16:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apis", "0017_leaverequest_rejection_reason"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="custom_user",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="employee",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]