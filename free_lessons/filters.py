from django_filters.rest_framework import FilterSet

from .models import Category, Course, Lesson, Comment, LikeDislike


class CategoryFilter(FilterSet):
    """
    Filter for Category model
    """
    class Meta:
        model = Category
        fields = ['name']


class CourseFilter(FilterSet):
    """
    Filter for Course model
    """
    class Meta:
        model = Course
        fields = ['name']


class LessonFilter(FilterSet):
    """
    Filter for Lesson model
    """
    class Meta:
        model = Lesson
        fields = ['name', 'created_at', 'updated_at']


class CommentFilter(FilterSet):
    """
    Filter for Comment model
    """
    class Meta:
        model = Comment
        fields = ['created_at', 'updated_at', 'lesson']


class LikeDislikeFilter(FilterSet):
    """
    Filter for LikeDislike model
    """
    class Meta:
        model = LikeDislike
        fields = ['like_dislike']