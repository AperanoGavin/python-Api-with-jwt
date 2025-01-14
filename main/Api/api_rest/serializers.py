from rest_framework import serializers
from Api.models import Movie , StreamPlatform

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model= Movie
        fields = "__all__"
        
        
    def validate_description(self , value):
        if len(value) < 10:
            raise serializers.ValidationError('no the good len')
        return value


class StreamPlatformSerializer( serializers.ModelSerializer):
    class Meta:
        model= StreamPlatform
        fields= "__all__"

''' class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    def create(self , validated_data):
        return Movie.objects.create(**validated_data)
    
    
    def update(self ,instance , validated_data):
        instance.name = validated_data.get('name' , instance.name)
        instance.description = validated_data.get('description' , instance.description)
        instance.active = validated_data.get('active' , instance.active)
        instance.save
        return instance
    
    def validate_description(self , value):
        if len(value) < 10:
            raise serializers.ValidationError('no the good len')
        return value
         '''