from django.db import models


class Exercises(models.Model):
    exercises_number_one = models.TextField()
    exercises_number_two = models.TextField()


class HandExercises(Exercises):  # упражнения для рук
    pass


class EyeExercises(Exercises):  # упражнения для глаз
    pass


class NeckExercises(Exercises):  # упражнения для шеи
    pass

