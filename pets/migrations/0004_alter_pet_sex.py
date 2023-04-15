# Generated by Django 4.2 on 2023-04-15 20:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0003_alter_pet_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="sex",
            field=models.CharField(
                choices=[
                    ("Male", "Male"),
                    ("Female", "Female"),
                    ("Not Informed", "Default"),
                ],
                default="Not Informed",
                max_length=20,
            ),
        ),
    ]
