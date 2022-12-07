# Generated by Django 4.1.3 on 2022-12-06 13:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='bookmarks',
            field=models.ManyToManyField(related_name='article_bookmarks', to=settings.AUTH_USER_MODEL),
        ),
    ]