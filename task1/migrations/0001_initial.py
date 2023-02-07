# Generated by Django 4.1.5 on 2023-02-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Food",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("OrderDate", models.DateField()),
                ("Region", models.CharField(max_length=15)),
                ("City", models.CharField(max_length=20)),
                ("Category", models.CharField(max_length=20)),
                ("Product", models.CharField(max_length=20)),
                ("Quantity", models.IntegerField()),
                ("UnitPrice", models.FloatField()),
            ],
        ),
    ]
