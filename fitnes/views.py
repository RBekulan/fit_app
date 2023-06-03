from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
import datetime

class EyeTrainingView(APIView):
    def get(self, request):
        training = EyeExercises.objects.all()
        serializer = EyeExercisesSerializers(training, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class HandTrainingView(APIView):
    def get(self, request):
        training = HandExercises.objects.all()
        serializer = HandExercisesSerializers(training, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class NeckTrainingView(APIView):
    def get(self, request):
        training = NeckExercises.objects.all()
        serializer = NeckExercisesSerializers(training, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class StartStopView(APIView):
    def get(self, request):
        start = datetime.datetime.now()
        stop = datetime.datetime.now()
        result = start - stop
        day = []
        day.append(result)
        return Response(data=f'результат {result}', status=status.HTTP_200_OK)

