from django.shortcuts import render

from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import (Category, Course, Lesson, Comment, LikeDislike, EmailSender)
from .serializers import (CategorySerializer, CourseSerializer, LessonSerializer,
                          CommentSerializer, LikeDislikeSerializer, EmailSenderSerializer)
from .permissions import (IsAdminOrReadOnly, IsAuthorOrReadOnly, IsUserOrReadOnly)
from .filters import (CategoryFilter, CourseFilter, LessonFilter, CommentFilter, LikeDislikeFilter)
from .paginations import (CoursePagination, LessonPagination, CommentPagination)


# Create your views here.


class CategoryViewSet(ModelViewSet):
    """
    A view designed for objects in the Category model using the ModelViewSet,
    filtering, searching, and ordering functions.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CategoryFilter
    search_fields = ['name']
    ordering_fields = ['name']


class CourseViewSet(ModelViewSet):
    """
    A view designed for objects in the Course model using the ModelViewSet,
    filtering, searching, and ordering functions.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    pagination_class = CoursePagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CourseFilter
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'category_id']


class LessonViewSet(ModelViewSet):
    """
    A view designed for objects in the Lesson model using the ModelViewSet,
    filtering, searching, and ordering functions.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = LessonFilter
    search_fields = ['name', 'text', 'course_name']
    ordering_fields = ['name', 'created_at', 'updated_at']
    pagination_class = LessonPagination


class CommentViewSet(ModelViewSet):
    """
    A view designed for objects in the Comment model using the ModelViewSet,
    filtering, searching, and ordering functions.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CommentFilter
    search_fields = ['name', 'author']
    ordering_fields = ['name', 'author', 'created_at', 'updated_at']
    pagination_class = CommentPagination


class LikeDislikeViewSet(ModelViewSet):
    """
    A view designed for objects in the LikeDislike model using the ModelViewSet.
    """
    queryset = LikeDislike.objects.all()
    serializer_class = LikeDislikeSerializer
    permission_classes = [IsUserOrReadOnly, IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = LikeDislikeFilter
    search_fields = ['lesson']
    ordering_fields = ['like_dislike']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class EmailSenderViewSet(ModelViewSet):
    """
    A view designed for objects in the EmailSender model using the ModelViewSet,
    """
    queryset = EmailSender.objects.all()
    serializer_class = EmailSenderSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication, SessionAuthentication]



