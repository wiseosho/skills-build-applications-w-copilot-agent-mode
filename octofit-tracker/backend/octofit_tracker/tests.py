from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser', email='testuser@example.com', password='password')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username='testuser', email='testuser@example.com', password='password')
        activity = Activity.objects.create(user=user, activity_type='Running', duration='01:00:00')
        self.assertEqual(activity.activity_type, 'Running')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create(username='testuser', email='testuser@example.com', password='password')
        leaderboard_entry = Leaderboard.objects.create(user=user, score=100, rank=1)
        self.assertEqual(leaderboard_entry.score, 100)
        self.assertEqual(leaderboard_entry.rank, 1)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(username='testuser', email='testuser@example.com', password='password')
        workout = Workout.objects.create(user=user, workout_type='Running', duration='01:00:00', calories_burned=500)
        self.assertEqual(workout.workout_type, 'Running')
        self.assertEqual(workout.calories_burned, 500)