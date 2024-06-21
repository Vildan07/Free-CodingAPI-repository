from django.contrib import admin

from .models import (Category, Course, Lesson, Comment, LikeDislike, EmailSender)

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    This class uses the Category model and registers
    it on the administrator's site.
    """
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    This class uses the Course model and registers
    it on the administrator's site.'
    """
    list_display = ('name', 'category', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """
    This class uses the Lesson model and registers
    it on the administrator's site.'
    """
    list_display = ('name', 'course', 'text', 'created_at', 'updated_at', 'slug', 'video')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    This class uses the Comment model and registers
    it on the administrator's site.'
    """
    list_display = ('author', 'lesson', 'text_length', 'created_at', 'updated_at')
    list_filter = ('author', 'lesson', 'text')
    list_display_links = ('author', 'lesson')

    def text_length(self, obj):
        return obj.text[:40]

    text_length.short_description = 'Text'


@admin.register(LikeDislike)
class LikeDislikeAdmin(admin.ModelAdmin):
    """
    This class uses the LikeDislike model and registers
    it on the administrator's site.'
    """
    list_display = ('lesson', 'user', 'like_dislike')
    list_filter = ('lesson', 'user', 'like_dislike')
    list_display_links = ('lesson', 'user')


@admin.register(EmailSender)
class EmailSenderAdmin(admin.ModelAdmin):
    """
    This class uses the EmailSender model and registers
    it on the administrator's site.'
    """
    list_display = ('message', 'created_at')
    list_filter = ('created_at',)





