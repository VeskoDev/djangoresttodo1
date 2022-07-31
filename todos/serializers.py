from rest_framework.serializers import ModelSerializer 
from todos.models import Todo, Movie

class TodoSerializer(ModelSerializer):
    
    class Meta:
        model=Todo
        fields = ('id','title', 'description', 'is_complete',)


class MovieSerializer(ModelSerializer):

    class Meta:
        model = Movie
        fields = ['title', 'description']
