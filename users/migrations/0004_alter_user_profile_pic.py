# Generated by Django 4.1.3 on 2022-12-10 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_pic",
            field=models.ImageField(
                default="placeholder_profile_image.png", upload_to=""
            ),
        ),
    ]
