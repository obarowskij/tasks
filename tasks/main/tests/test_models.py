import pytest
from main.models import Task
from django.urls import reverse
from rest_framework.test import APIClient

TASK_URL = reverse("task-list")

@pytest.mark.django_db
def test_task_model(create_task):
    task = create_task(name="Test Task")
    assert task.name == "Test Task"
    assert task.status == "N"
    assert len(Task.objects.all()) == 1


def test_auth_required():
    client = APIClient()

    res = client.get(TASK_URL)
    assert res.status_code == 401

@pytest.mark.django_db
def test_auth_works(authenticated_client):
    res = authenticated_client.get(TASK_URL)
    assert res.status_code == 200

@pytest.mark.django_db
def test_create_task(authenticated_client):
    res = authenticated_client.post(TASK_URL, {"name": "Test Task"})
    assert res.status_code == 201
    assert Task.objects.get(name="Test Task")
    assert Task.objects.count() == 1

@pytest.mark.django_db
def test_create_task_unauthenticated():
    client = APIClient()
    res = client.post(TASK_URL, {"name": "Test Task"})
    assert res.status_code == 401
    assert Task.objects.count() == 0

@pytest.mark.django_db
def test_update_task(authenticated_client, create_task):
    task = create_task(name="Test Task")
    url = reverse("task-detail", kwargs={"pk": task.pk})
    res = authenticated_client.patch(url, {"name": "Updated Task"})
    assert res.status_code == 200
    assert Task.objects.get(name="Updated Task")

@pytest.mark.django_db
def test_delete_task(authenticated_client, create_task):
    task = create_task(name="Test Task")
    url = reverse("task-detail", kwargs={"pk": task.pk})
    res = authenticated_client.delete(url)
    assert res.status_code == 204
    assert Task.objects.count() == 0

@pytest.mark.django_db
def test_filter_tasks(authenticated_client, create_task):
    create_task(name="Test Task 1")
    create_task(name="Test Task 2")
    res = authenticated_client.get(TASK_URL + "?name=Test Task 1")
    assert res.status_code == 200
    assert len(res.data) == 1
    assert res.data[0]["name"] == "Test Task 1"

@pytest.mark.django_db
def test_filtering_tasks_by_desc(authenticated_client, create_task):
    create_task(name="Test Task 1", description="Test description")
    create_task(name="Test Task 2", description="Another description")
    res = authenticated_client.get(TASK_URL + "?description=Test description")
    assert res.status_code == 200
    assert len(res.data) == 1
    assert res.data[0]["name"] == "Test Task 1"