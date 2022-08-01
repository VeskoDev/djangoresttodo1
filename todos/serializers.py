from rest_framework.serializers import ModelSerializer
from todos.models import Todo, Movie, Tag, Participant


class TodoSerializer(ModelSerializer):
    
    class Meta:
        model=Todo
        fields = ('id','title', 'description', 'is_complete',)



class TagSerializer(ModelSerializer):
    
     class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_field = ['id']



class MovieSerializer(ModelSerializer):

    tags = TagSerializer(many = True, required = True)
    class Meta:
        model = Movie
        fields = ['title', 'description', 'tags']

    def _get_or_create_tags(self, tags, movie):
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(**tag)
            movie.tags.add(tag_obj)

    def create(self, validated_data):
            tags = validated_data.pop('tags', [])
            movie = Movie.objects.create(**validated_data)
            self._get_or_create_tags(tags, movie)
            
            return movie
        
    def update(self, instance, validated_data):
            """Update recipe"""
            tags = validated_data.pop('tags', None)
            if tags is not None:
                instance.tags.clear()
                self._get_or_create_tags(tags, instance)

            for attr, value in validated_data.items():
                setattr(instance, attr, value)
                
            instance.save()
            return instance 



class ParticipantSerializer(ModelSerializer):
    
     class Meta:
        model = Participant
        fields = ['id', 'name', 'last_name', 'date_of_birth', 'description', 'title']
        read_only_field = ['id']

        
