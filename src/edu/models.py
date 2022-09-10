from django.db import models
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class Homework(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    student = models.CharField(max_length=128)
    data = models.TextField()
    deadline = models.DateField()
