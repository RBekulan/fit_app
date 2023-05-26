from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.contrib.auth.models import User

from django.shortcuts import render


@api_view(['POST'])
def pro_version(request):
    serializers = ValidateSerializers(data=request.data)
    if not serializers.is_valid():
        return Response(data={'errors': serializers.errors}, status=status.HTTP_400_BAD_REQUEST)
    name_card = request.data.get('name_card')
    cvc_card = request.data.get('cvc_card')
    valid_thru = request.data.get('valid_thru')
    number_card = request.data.get('number_card')
    money = request.data.get('money')
    pro = ProUser.objects.create(name_card=name_card, cvc_card=cvc_card, valid_thru=valid_thru,
                                 number_card=number_card,
                                 money=money)
    pro.is_active = True

    return Response(data=ProUserSerializers(pro).data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def training_leg(request):
    if User(is_active=True):
        training = LegExercises.objects.all()
        serializer = LegExercisesSerializers(training, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
        (render('localhost/api/v1/plusversion/'))


@api_view(['GET'])
def training_back(request):
    if User(is_active=True):
        training = BackExercises.objects.all()
        serializer = BackExercisesSerializers(training, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
        (render('localhost/api/v1/plusversion/'))
