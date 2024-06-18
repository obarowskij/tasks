from django.urls import path, include
from rest_framework import routers

from .views import TaskViewSet, CreateUserViewSet

router = routers.DefaultRouter()

router.register(r"tasks", TaskViewSet, basename="task")
router.register(r"create_user", CreateUserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls"))
]