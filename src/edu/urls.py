from rest_framework.routers import SimpleRouter

from edu.views import HomeworkModelViewSet


app_name = "edu"

homework_router = SimpleRouter()
homework_router.register(r'homework', HomeworkModelViewSet, basename='homework')

urlpatterns = homework_router.urls
