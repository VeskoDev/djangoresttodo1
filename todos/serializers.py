from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from todos.models import Todo, Movie, Participant, Title, Slike, PrikazSlika
#Programmer, Language, Paradigm, Tag, TagImage


class TodoSerializer(ModelSerializer):
    
    class Meta:
        model=Todo
        fields = ('id','title', 'description', 'is_complete',)


# class TagImageSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = TagImage
#         fields = '__all__'

# class TagSerializer(serializers.HyperlinkedModelSerializer):
    
#      class Meta:
#         model = Tag
#         fields = '__all__'



        #read_only_field = ['id']
    
    #  def create(self, validated_data):
    #         images_data = validated_data.pop('images')
    #         tag = Tag.objects.create(**validated_data)
    #         for image_data in images_data:
    #             TagImage.objects.create(tag=tag, **image_data)
    #         return tag



class TitleSerializer(serializers.HyperlinkedModelSerializer):
    
     class Meta:
        model = Title
        fields = ['id', 'name']
        read_only_field = ['id']


class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    
     class Meta:
        model = Participant
        fields = '__all__'
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

   