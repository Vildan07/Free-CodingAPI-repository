from django.urls import path, include

from .views import (CategoryViewSet, CourseViewSet, LessonViewSet, CommentViewSet, LikeDislikeViewSet,
                    EmailSenderViewSet)

from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('course', CourseViewSet)
router.register('lesson', LessonViewSet)
router.register('comment', CommentViewSet)
router.register('like-dislike', LikeDislikeViewSet)
router.register('email-sender', EmailSenderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]