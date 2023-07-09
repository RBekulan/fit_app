from .models import Exercises, NameCategory
from rest_framework import serializers
from .models import *


class NameCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = NameCategory
        fields = '__all__'


class StudentsSerializers(serializers.ModelSerializer):
    school = NameCategorySerializers()

    class Meta:
        model = Exercises
        fields = '__all__'


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
