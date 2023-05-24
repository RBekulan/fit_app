from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import *


@api_view(['GET'])
def training_eye(request):
    training = EyeExercises.objects.all()
    serializer = EyeExercisesSerializers(training, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def training_hand(request):
    training = HandExercises.objects.all()
    serializer = HandExercisesSerializers(training, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def training_neck(request):
    training = NeckExercises.objects.all()
    serializer = NeckExercisesSerializers(training, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def training_leg(request):
    training = LegExercises.objects.all()
    serializer = LegExercisesSerializers(training, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def training_back(request):
    training = BackExercises.objects.all()
    serializer = BackExercisesSerializers(training, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
