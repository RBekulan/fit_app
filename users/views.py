from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from users.serializers import UserLoginValidateSerializer, UserCreateValidateSerializer

class AuthorizationView(APIView):
    def post(self, request):
        serializer = UserLoginValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={'errors': 'пароль или логин'})

class RegisterView(APIView):
    def post(self, request):
        serializer = UserCreateValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data, is_active=False)
        user.save()
        return Response(status=status.HTTP_201_CREATED, data={'user_id': user.id})
