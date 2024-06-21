from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Category, Course, Lesson, Comment, LikeDislike, EmailSender


class CategorySerializer(serializers.ModelSerializer):
    """
    This Serializer serializes the Category model
    """
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class CourseSerializer(serializers.ModelSerializer):
    """
    This Serializer serializes the Course model
    """
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="name"
    )

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    """
    This Serializer serializes the Lesson model
    """
    course = serializers.SlugRelatedField(
        queryset=Course.objects.all(), slug_field="name"
    )

    class Meta:
        model = Lesson
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """
    This Serializer serializes the Comment model
    """
    lesson = serializers.SlugRelatedField(
        queryset=Lesson.objects.all(), slug_field="name",
        write_only=True, allow_null=True
    )
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author',)


class LikeDislikeSerializer(serializers.ModelSerializer):
    """
    This Serializer serializes the LikeDislike model
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = LikeDislike
        fields = '__all__'
        read_only_fields = ('author',)


class EmailSenderSerializer(serializers.ModelSerializer):
    """
    This Serializer serializes the EmailSender model
    """
    class Meta:
        model = EmailSender
        fields = '__all__'
