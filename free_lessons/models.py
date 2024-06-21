from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator, RegexValidator, MaxLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .utils import send_message_email


# Create your models here.


class Category(models.Model):
    """
    This model for Categories in our free courses
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


class Course(models.Model):
    """
    This model for Courses in Categories in our free courses
    """
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    slug = models.SlugField(default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['-pk']


class Lesson(models.Model):
    """
    This model for Lessons in Courses in our free Courses
    """
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    video = models.FileField(upload_to='videos/', validators=[FileExtensionValidator(
                                allowed_extensions=['mp4', 'mov', 'avi', 'webm'],
                                message='Only mp4, mov, webm and avi are supported.')])
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default=None)

    def __str__(self):
        return f"Course: {self.course} / Lesson: {self.name}"

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
        ordering = ['-pk']


class Comment(models.Model):
    """
    This model is for comments on our lessons
    """
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    text = models.TextField(validators=[MaxLengthValidator(1000)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.lesson}"

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-pk']


LIKE_DISLIKE = (
    ('like', 'like'),
    ('dislike', 'dislike'),
    ('NULL', 'NULL')
)


class LikeDislike(models.Model):
    """
    This model is for evaluating lessons in courses
    """
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    like_dislike = models.CharField(max_length=15, choices=LIKE_DISLIKE, default='NULL')

    def __str__(self):
        return f"{self.lesson} / {self.like_dislike}"


class EmailSender(models.Model):
    """
    This model is for sending emails to users
    """
    email_address = models.ManyToManyField(User)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email_address}: {self.created_at}'


@receiver(post_save, sender=EmailSender)
def send_message(sender, instance, created, **kwargs):
    """
    This function is to send a notification about update informations
    """
    if created:
        users = User.objects.all()
        subject = f"Message: {instance.email_address}"
        message = instance.message
        for user in users:
            send_message_email(user.email, subject, message)

