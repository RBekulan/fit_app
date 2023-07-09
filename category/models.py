from django.db import models


class NameCategory(models.Model):
    image = models.ImageField()
    name = models.TextField(max_length=230)

    def __str__(self):
        return self.name


class Exercises(models.Model):
    name_category = models.ForeignKey(NameCategory, on_delete=models.CASCADE, null=True,)
    name_exercises = models.CharField(max_length=234)
    description = models.TextField()
    image = models.ImageField()


    def __str__(self):
        return self.name_exercises


class HandExercises(Exercises):  # упраmжнения для рук
    pass


class EyeExercises(Exercises):  # упражнения для глаз
    pass


class NeckExercises(Exercises):  # упражнения для шеи
    pass

