from django.urls import path

from edu.views import HomeworkCreateAPIView, HomeworkListAPIView


app_name = "edu"


urlpatterns = [
    path(
        '',
        HomeworkListAPIView.as_view(),
        name='homework-list'
    ),
    path(
        'create/',
        HomeworkCreateAPIView.as_view(),
        name='homework-create'
    ),
]
