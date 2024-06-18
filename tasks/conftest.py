# conftest.py
import os
import pytest
from django.contrib.auth.models import User
import django
from main.models import Task
from rest_framework.test import APIClient

django.setup()

@pytest.fixture
def create_task():
    def make_task(**kwargs):
        return Task.objects.create(**kwargs)
    return make_task


@pytest.fixture
def authenticated_client():
    user = User.objects.create_user(username='testuser', password='12345')
    client = APIClient()
    client.force_authenticate(user=user)
    return client
