# Generated by Django 4.1.3 on 2022-12-12 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0007_alter_image_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="image",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AddField(
            model_name="imagealbum",
            name="slug",
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
