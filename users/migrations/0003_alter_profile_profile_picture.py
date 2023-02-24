# Generated by Django 4.1.6 on 2023-02-24 16:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="profile_pictures/%Y/%m/%d/"
            ),
        ),
    ]
