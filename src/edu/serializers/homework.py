from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Homework


UserModel = get_user_model()


class HomeworkSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=UserModel.objects.all()
    )

    class Meta:
        model = Homework
        fields = "__all__"
