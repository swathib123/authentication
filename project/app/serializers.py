
from rest_framework import serializers
from .models import Manager
from django.contrib.auth import authenticate
from rest_framework import serializers

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        manager = Manager(**validated_data)
        manager.set_password(validated_data['password'])  # Hash the password
        manager.save()
        return manager
    



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid username or password.")

        attrs['user'] = user
        return attrs
