from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    id_student = models.IntegerField()
    gpa = models.FloatField()
    rating = models.FloatField()
    photo = models.ImageField()