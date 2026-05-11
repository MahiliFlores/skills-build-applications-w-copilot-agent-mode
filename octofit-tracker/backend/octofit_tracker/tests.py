from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import User, Team, Activity, Workout, Leaderboard

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name="Equipo Test")
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="testpass", team=self.team)
        self.client.force_authenticate(user=self.user)
        self.workout = Workout.objects.create(name="Cardio", description="Ejercicio de cardio", difficulty="Fácil")
        self.activity = Activity.objects.create(user=self.user, type="Correr", duration=30, calories=200)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=100)

    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.data)

    def test_user_list(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, 200)

    def test_team_list(self):
        response = self.client.get(reverse('team-list'))
        self.assertEqual(response.status_code, 200)

    def test_activity_list(self):
        response = self.client.get(reverse('activity-list'))
        self.assertEqual(response.status_code, 200)

    def test_workout_list(self):
        response = self.client.get(reverse('workout-list'))
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_list(self):
        response = self.client.get(reverse('leaderboard-list'))
        self.assertEqual(response.status_code, 200)
