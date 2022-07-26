from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todos.models import  Movie, Participant, Title, Slike, PrikazSlika, Tag

from rest_framework import permissions, filters, viewsets
from todos.serializers import  MovieSerializer, ParticipantSerializer, TitleSerializer, PrikazSlikaSerializer, SlikeSerializer, TagSerializer
#TodoSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


"""Handluje get i post metodu istovremeno za razliku ovog sto imamo dolje"""
# class TodosAPIView(ListCreateAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)

#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    

#     filterset_fields = ["id", 'title', 'is_complete']
#     search_fields = ["id", "title", 'is_complete']
#     ordering_fields = ["id", "title", 'is_complete']

#     def perform_create(self, serializer):
#         return serializer.save(owner=self.request.user)
    
#     def get_queryset(self):
#         return Todo.objects.filter(owner=self.request.user)


# class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     lookup_field = "id"



#     def get_queryset(self):
#         return Todo.objects.filter(owner=self.request.user)




class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'description']



class ParticipantViewSet(viewsets.ModelViewSet):
   
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class TitleViewSet(viewsets.ModelViewSet):
    """Maange tags in the datbase"""
    queryset = Title.objects.all()
    serializer_class = TitleSerializer



class SlikeView(viewsets.ModelViewSet):
    queryset = Slike.objects.all()
    serializer_class = SlikeSerializer

class PrikazSlikaView(viewsets.ModelViewSet):
    queryset = PrikazSlika.objects.all()
    serializer_class = PrikazSlikaSerializer

class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer