# Generated by Django 4.1.7 on 2023-05-10 07:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0012_alter_post_post_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="post_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
