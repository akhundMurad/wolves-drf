from django.db import models

class Homework(models.Model):
    author = models.CharField(max_length=128)
    student = models.CharField(max_length=128)
    data = models.TextField()
    deadline = models.DateField()
