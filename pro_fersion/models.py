from django.db import models


class ProUser(models.Model):
    number_card = models.CharField(max_length=230)
    cvc_card = models.CharField(max_length=230)
    valid_thru = models.CharField(max_length=230)
    name_card = models.CharField(max_length=230)
    money = models.CharField(max_length=230, default=500)


class LegExercises(models.Model):  # упражнения для ног
    warm_up = models.CharField(max_length=230)  # размика
    jumping = models.CharField(max_length=230)  # прыжки
    sit_ups = models.CharField(max_length=230)  # приседания


class BackExercises(models.Model):  # упражнения  спины
    hand_rotations = models.CharField(max_length=230)  # вращения руками
    pull_ups = models.CharField(max_length=230)  # подтягивание в турник
