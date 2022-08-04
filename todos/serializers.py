from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from todos.models import  Movie, Participant, Title, Slike, PrikazSlika


# class TodoSerializer(ModelSerializer):
    
#     class Meta:
#         model=Todo
#         fields = ('id','title', 'description', 'is_complete',)



class TitleSerializer(serializers.HyperlinkedModelSerializer):
    
     class Meta:
        model = Title
        fields = ['id', 'name']
        read_only_field = ['id']


class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    
     class Meta:
        model = Participant
        fields = ['name', 'last_name', 'date_of_birth', 'description', 'image_of_participant']
        read_only_field = ['id']





class MovieSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Movie
        fields = ['title', 'description',  'participants']
 

class PrikazSlikaSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = PrikazSlika
        fields = '__all__'
class SlikeSerializer(serializers.HyperlinkedModelSerializer):

    albums = PrikazSlikaSerializer(serializers.ModelSerializer, many=True, required=False)
    class Meta:
        model = Slike
        fields = ['name', 'albums']

   