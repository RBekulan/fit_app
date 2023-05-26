from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserValidateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=123)
    password = serializers.CharField(max_length=123)

    def validated_password(self, password):
        return password


class UserLoginValidateSerializer(UserValidateSerializer):
    pass


class UserCreateValidateSerializer(UserValidateSerializer):

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except:
            return username
        raise ValidationError(f'такой {username} уже есть')
