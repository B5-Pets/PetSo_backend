# Generated by Django 4.1.3 on 2022-12-22 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="email address"
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "profile_img",
                    models.ImageField(
                        blank=True, default="profile/default.jpeg", upload_to="profile"
                    ),
                ),
                ("introduce", models.TextField(blank=True, max_length=500)),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "followings",
                    models.ManyToManyField(
                        blank=True,
                        related_name="followers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Pet",
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
                ("pet_name", models.CharField(max_length=100, verbose_name="펫이름")),
                ("pet_age", models.PositiveIntegerField(null=True, verbose_name="펫나이")),
                (
                    "pet_sex",
                    models.CharField(max_length=100, null=True, verbose_name="펫성별"),
                ),
                (
                    "pet_species",
                    models.CharField(max_length=100, null=True, verbose_name="품종명"),
                ),
                ("pet_desc", models.CharField(max_length=200, verbose_name="설명")),
                (
                    "pet_image",
                    models.ImageField(
                        blank=True,
                        default="profile/default.jpeg",
                        upload_to="profile/pet",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="집사",
                    ),
                ),
            ],
        ),
    ]
