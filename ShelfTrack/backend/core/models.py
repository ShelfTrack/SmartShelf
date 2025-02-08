from django.db import models

class Student(models.Model):
    roll_no = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    division = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.roll_no} - {self.name} (Class {self.grade} {self.division})"
