from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todos.models import Todo, Movie, Tag, Participant, Title
#Language, Programmer, Paradigm
from rest_framework import permissions, filters, viewsets, mixins
from todos.serializers import TodoSerializer, MovieSerializer, TagSerializer, ParticipantSerializer, TitleSerializer
#LanguageSerializer, ProgrammerSerializer, ParadigmSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


"""Handluje get i post metodu istovremeno za razliku ovog sto imamo dolje"""
class TodosAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    

    filterset_fields = ["id", 'title', 'is_complete']
    search_fields = ["id", "title", 'is_complete']
    ordering_fields = ["id", "title", 'is_complete']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

# """Create API View automatski handluje post req"""
# class CreateTodoApiView(CreateAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = (IsAuthenticated,)


#     def perform_create(self, serializer):
#         return serializer.save(owner=self.request.user)


# class TodoListAPIView(ListAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = (IsAuthenticated,)


#     def get_queryset(self):
#         return Todo.objects.filter(owner=self.request.user)


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = "id"



    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)




class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'description','participants']


class TagViewSet(viewsets.ModelViewSet):
    """Maange tags in the datbase"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    """Maange tags in the datbase"""
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()


class TitleViewSet(viewsets.ModelViewSet):
    """Maange tags in the datbase"""
    queryset = Title.objects.all()
    serializer_class = TitleSerializer



# class LanguageView(viewsets.ModelViewSet):
#     queryset = Language.objects.all()
#     serializer_class = LanguageSerializer


# class ParadigmView(viewsets.ModelViewSet):
#     queryset = Paradigm.objects.all()
#     serializer_class = ParadigmSerializer


# class ProgrammerView(viewsets.ModelViewSet):
#     queryset = Programmer.objects.all()
#     serializer_class = ProgrammerSerializer
