# Generated by Django 4.1.3 on 2022-12-09 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0003_alter_image_album"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagealbum",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]