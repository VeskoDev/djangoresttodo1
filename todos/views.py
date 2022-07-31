from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todos.models import Todo, Movie, Tag
from rest_framework import permissions, filters, viewsets, mixins
from todos.serializers import TodoSerializer, MovieSerializer, TagSerializer
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
    lookup_field = 'pk'


class TagViewSet(mixins.CreateModelMixin,mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """Maange tags in the datbase"""
    serializer_class = TagSerializer
    queryset = Tag.objects.all()