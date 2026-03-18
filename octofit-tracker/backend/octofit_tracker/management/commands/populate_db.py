from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create test users
        user1 = User.objects.create(username='alice', email='alice@example.com', team='TeamA')
        user2 = User.objects.create(username='bob', email='bob@example.com', team='TeamA')
        user3 = User.objects.create(username='charlie', email='charlie@example.com', team='TeamB')

        # Create test teams
        teamA = Team.objects.create(name='TeamA')
        teamB = Team.objects.create(name='TeamB')
        teamA.members.add(user1, user2)
        teamB.members.add(user3)

        # Create test activities
        Activity.objects.create(user='alice', activity_type='run', duration=30, date='2026-03-18T08:00:00Z')
        Activity.objects.create(user='bob', activity_type='cycle', duration=45, date='2026-03-18T09:00:00Z')
        Activity.objects.create(user='charlie', activity_type='swim', duration=60, date='2026-03-18T10:00:00Z')

        # Create test leaderboard
        Leaderboard.objects.create(user='alice', score=120)
        Leaderboard.objects.create(user='bob', score=110)
        Leaderboard.objects.create(user='charlie', score=130)

        # Create test workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='Easy')
        Workout.objects.create(name='Squats', description='Do 30 squats', difficulty='Medium')
        Workout.objects.create(name='Burpees', description='Do 15 burpees', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('Test data populated in octofit_db database'))
