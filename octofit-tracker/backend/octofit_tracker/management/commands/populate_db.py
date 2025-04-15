from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(_id=ObjectId(), username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
            User(_id=ObjectId(), username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
            User(_id=ObjectId(), username='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword'),
            User(_id=ObjectId(), username='crashoverride', email='crashoverride@mhigh.edu', password='crashoverridepassword'),
            User(_id=ObjectId(), username='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(_id=ObjectId(), name='Blue Team'),
            Team(_id=ObjectId(), name='Gold Team'),
        ]
        for team in teams:
            team.save()

        # Add members to teams
        teams[0].members.add(users[0], users[1])
        teams[1].members.add(users[2], users[3], users[4])

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Cycling', duration=timedelta(hours=1)),
            Activity(_id=ObjectId(), user=users[1], activity_type='Crossfit', duration=timedelta(hours=2)),
            Activity(_id=ObjectId(), user=users[2], activity_type='Running', duration=timedelta(hours=1, minutes=30)),
            Activity(_id=ObjectId(), user=users[3], activity_type='Strength', duration=timedelta(minutes=30)),
            Activity(_id=ObjectId(), user=users[4], activity_type='Swimming', duration=timedelta(hours=1, minutes=15)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], score=100, rank=1),
            Leaderboard(_id=ObjectId(), user=users[1], score=90, rank=2),
            Leaderboard(_id=ObjectId(), user=users[2], score=95, rank=3),
            Leaderboard(_id=ObjectId(), user=users[3], score=85, rank=4),
            Leaderboard(_id=ObjectId(), user=users[4], score=80, rank=5),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), user=users[0], workout_type='Cycling Training', duration=timedelta(hours=1), calories_burned=500),
            Workout(_id=ObjectId(), user=users[1], workout_type='Crossfit', duration=timedelta(hours=2), calories_burned=800),
            Workout(_id=ObjectId(), user=users[2], workout_type='Running Training', duration=timedelta(hours=1, minutes=30), calories_burned=600),
            Workout(_id=ObjectId(), user=users[3], workout_type='Strength Training', duration=timedelta(minutes=30), calories_burned=300),
            Workout(_id=ObjectId(), user=users[4], workout_type='Swimming Training', duration=timedelta(hours=1, minutes=15), calories_burned=700),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))