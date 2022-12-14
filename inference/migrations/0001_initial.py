# Generated by Django 4.1.3 on 2022-12-14 08:17

from django.db import migrations, models
import django_base64field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Inference",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "output_img",
                    django_base64field.fields.Base64Field(
                        blank=True, default="", max_length=900000, null=True
                    ),
                ),
            ],
        ),
    ]
