from django.db import models

# Create your models here.
from django.db import models
from users.models import Student

class Course(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.code

class ClassRoutine(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    time = models.CharField(max_length=20)
    room = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.course.code} - {self.day}"

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    ct1 = models.IntegerField()
    ct2 = models.IntegerField()
    mid = models.IntegerField()
    final = models.IntegerField()

    def __str__(self):
        return f"{self.student.user.username} - {self.course.code}"