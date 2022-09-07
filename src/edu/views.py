from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.request import Request
from django.db.models import QuerySet

from edu.models import Homework


class HomeworkCreateAPIView(CreateAPIView):
    class InputSerializer(serializers.Serializer):
        author = serializers.CharField(required=True)
        student = serializers.CharField(required=True)
        data = serializers.CharField(required=True)
        deadline = serializers.DateField(required=True)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Homework
            fields = ['data', 'deadline']

    def create(self, request: Request, *args, **kwargs) -> Response:
        serialized = self.InputSerializer(
            data=request.data
        )
        serialized.is_valid(raise_exception=True)

        homework = Homework.objects.create(
            **serialized.validated_data
        )

        return Response(
            data=self.OutputSerializer(homework).data,
            status=201
        )


class HomeworkListAPIView(ListAPIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Homework
            fields = ['data', 'deadline', 'student']

    def get_queryset(self) -> QuerySet:
        return Homework.objects.get_queryset()

    serializer_class = OutputSerializer
