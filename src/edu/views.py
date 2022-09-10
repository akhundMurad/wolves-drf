from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from edu.models import Homework
from edu.serializers.homework import HomeworkSerializer


class HomeworkModelViewSet(ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=["POST"], detail=False)
    def bulk_create(self, request: Request) -> Response:
        data = request.data
        prepared_objects = self.get_prepared_items(data)

        created_objects = Homework.objects.bulk_create(prepared_objects)
        return Response(
            status=201,
            data=self.get_serializer(created_objects, many=True).data
        )

    def get_prepared_items(self, data: list[dict]) -> list:
        serializer = self.get_serializer_class()
        prepared_objects = []

        if not isinstance(data, list):
            raise ValidationError('Request data must be an array.')

        for item in data:
            serialized = serializer(data=item)
            if serialized.is_valid(raise_exception=True):
                data = serialized.validated_data
                data.update({
                    'id': item.get('id', None)
                })
                instance = Homework(**data)

                prepared_objects.append(instance)

        return prepared_objects
