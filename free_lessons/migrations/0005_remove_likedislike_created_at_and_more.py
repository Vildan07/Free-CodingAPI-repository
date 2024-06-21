# Generated by Django 5.0.6 on 2024-06-20 16:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free_lessons', '0004_alter_category_options_alter_comment_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likedislike',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='likedislike',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='likedislike',
            name='like',
        ),
        migrations.RemoveField(
            model_name='likedislike',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='likedislike',
            name='like_dislike',
            field=models.CharField(choices=[('like', 'like'), ('dislike', 'dislike')], default='Like', max_length=15),
        ),
        migrations.AlterField(
            model_name='likedislike',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='free_lessons.lesson'),
        ),
        migrations.AlterField(
            model_name='likedislike',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
