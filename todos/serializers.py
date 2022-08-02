from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from todos.models import Todo, Movie, Tag, Participant, Title
#Programmer, Language, Paradigm


class TodoSerializer(ModelSerializer):
    
    class Meta:
        model=Todo
        fields = ('id','title', 'description', 'is_complete',)



class TagSerializer(serializers.HyperlinkedModelSerializer):
    
     class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_field = ['id']



class TitleSerializer(serializers.HyperlinkedModelSerializer):
    
     class Meta:
        model = Title
        fields = ['id', 'name', 'participants']
        read_only_field = ['id']


class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    

     class Meta:
        model = Participant
        fields = ['id', 'name', 'last_name', 'description', 'titles']
        read_only_field = ['id']


# class LanguageSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = Language
#         fields = ('id', 'url', 'name', 'paradigm')



# class ParadigmSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = Paradigm
#         fields = ('id', 'name')

# class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    
#     class Meta:
#         model = Programmer
#         fields = ('id','name', 'language')


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Movie
        fields = ['title', 'description',  'participants', 'tag']
 

