# Generated by Django 4.1.5 on 2023-01-28 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0003_rename_listing_type_listing_listing_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="picture1",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]