from rest_framework import serializers
from .models import Student

class Testserializers(serializers.Serializer):
    name=serializers.CharField()
    address=serializers.CharField()
    is_user1=serializers.BooleanField()
    
    def create(self,**validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
    
    