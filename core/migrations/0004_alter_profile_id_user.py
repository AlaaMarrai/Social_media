# Generated by Django 4.1.7 on 2023-05-07 19:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_profile_id_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="id_user",
            field=models.IntegerField(),
        ),
    ]
