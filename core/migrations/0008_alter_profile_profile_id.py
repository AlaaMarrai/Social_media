# Generated by Django 4.1.7 on 2023-05-07 22:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0007_profile_birth_date_profile_id_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
