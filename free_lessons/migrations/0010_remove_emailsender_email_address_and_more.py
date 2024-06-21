# Generated by Django 5.0.6 on 2024-06-20 18:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free_lessons', '0009_remove_emailsender_title_emailsender_email_address'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailsender',
            name='email_address',
        ),
        migrations.AddField(
            model_name='emailsender',
            name='email_address',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]