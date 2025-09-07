# tasks/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task

User = get_user_model()

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", email="test@test.com", password="password123")
        self.client.force_authenticate(user=self.user)
        self.task = Task.objects.create(
            user=self.user,
            title="Test Task",
            description="Test Description",
            status="pending"
        )

    def test_create_task(self):
        data = {"title": "New Task", "description": "New Description", "status": "pending"}
        response = self.client.post("/api/tasks/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_list_tasks(self):
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_recent_completed_tasks(self):
        self.task.status = "completed"
        self.task.save()
        response = self.client.get("/api/tasks/recent-completed/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
