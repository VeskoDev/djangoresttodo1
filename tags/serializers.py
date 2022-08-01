
from rest_framework.serializers import ModelSerializer
from .models import Tag
from todos.serializers import MovieSerializer


class TagSerializer(ModelSerializer):
    
     
     class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_field = ['id']
