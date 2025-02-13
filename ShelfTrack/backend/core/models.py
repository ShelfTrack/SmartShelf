from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    roll_no = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    grade = models.CharField(max_length=10)
    division = models.CharField(max_length=5)

    class Meta:
        unique_together = ("roll_no","grade","divsion")
    
    def _str_(self):
        return f"{self.roll_no} - {self.name} (Class {self.grade} {self.division})"
