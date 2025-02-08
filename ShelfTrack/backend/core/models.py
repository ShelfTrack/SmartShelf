from django.db import models

class Student(models.Model):
    roll_no = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    div = models.CharField(max_length=2)
    