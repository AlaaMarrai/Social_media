# Generated by Django 4.1.7 on 2023-05-07 21:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_alter_profile_id_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="birth_date",
        ),
    ]
