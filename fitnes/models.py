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


class LegExercises(models.Model):  # упражнения для ног
    warm_up = models.CharField(max_length=230)  # размика
    jumping = models.CharField(max_length=230)  # прыжки
    sit_ups = models.CharField(max_length=230)  # приседания


class BackExercises(models.Model):
    hand_rotations = models.CharField(max_length=230)  # вращения руками
    pull_ups = models.CharField(max_length=230)  # подтягивание в турник
