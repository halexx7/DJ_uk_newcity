# Generated by Django 2.2.24 on 2021-08-22 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("personalacc", "0002_auto_20210822_2114"),
    ]

    operations = [
        migrations.AlterField(
            model_name="siteconfiguration",
            name="image",
            field=models.ImageField(
                default="slide_1.jpg",
                help_text="Изображение которое отображается на главной странице",
                upload_to="Изображение",
                verbose_name="Главное изображение",
            ),
        ),
    ]
