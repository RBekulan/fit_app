from rest_framework import serializers
from .models import *


class EyeExercisesSerializers(serializers.ModelSerializer):
    class Meta:
        model = EyeExercises
        fields = '__all__'


class HandExercisesSerializers(serializers.ModelSerializer):
    class Meta:
        model = HandExercises
        fields = '__all__'


class NeckExercisesSerializers(serializers.ModelSerializer):
    class Meta:
        model = NeckExercises
        fields = '__all__'


class LegExercisesSerializers(serializers.ModelSerializer):
    class Meta:
        model = LegExercises
        fields = '__all__'


class BackExercisesSerializers(serializers.ModelSerializer):
    class Meta:
        model = BackExercises
        fields = '__all__'
