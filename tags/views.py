from django.shortcuts import render
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todos.models import Todo, Movie, Tag
from rest_framework import permissions, filters, viewsets, mixins
from todos.serializers import TodoSerializer, MovieSerializer, TagSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class TagViewSet(mixins.CreateModelMixin,mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """Maange tags in the datbase"""
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

