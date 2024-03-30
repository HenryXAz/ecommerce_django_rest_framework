# rest framework
from rest_framework import serializers

# models
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password'],
        }


class TestUserSerializer(serializers.Serializer):
    """Test serializer"""
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    def validate_name(self, value):
        if 'develop' in value:
            raise serializers.ValidationError('Error, no puede existir un usuario con ese nombre') 
        return value

    def validate_email(self, value):
        print(value)
        return value

    def validate(self, data):
        return data
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)

        instance.save()
        return instance

