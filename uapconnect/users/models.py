from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_no = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    batch = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username