from rest_framework import serializers
from .models import Student

class Testserializers(serializers.Serializer):
    name=serializers.CharField(error_messages={'blank':'Name cannot be blank Understand','required':'Name is required'})
    address=serializers.CharField()
    age=serializers.IntegerField()
    mobile_num=serializers.CharField(max_length=15)
    # is_user1=serializers.BooleanField()
    
    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
    
    # for validation different field called Field Validation
    
    def validate_age(self,age):
        print("noifasndogfnm")
        if age < 0 or age >= 100:
            print("noifasndogfnm")
            raise serializers.ValidationError("Sorry age must be lie in that range 1-99")
        return age
    
    def validate_mobile_num(self,num):
        print('done',num)
        if Student.objects.filter(mobile_num=num):
            raise serializers.ValidationError("Mobile number already exists")
        return num
