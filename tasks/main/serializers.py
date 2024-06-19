from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Task


class TaskHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Task.history.model
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    history = TaskHistorySerializer(many=True, required=False)
    class Meta:
        model = Task
        fields = ["id", "name", "description", "status", "assigned_user", "history"]
        readonly_filds = ["id", "history"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = get_user_model().objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
