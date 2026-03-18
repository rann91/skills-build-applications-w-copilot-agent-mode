from djongo import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100, blank=True, null=True)

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE, related_name='team_members')

class Activity(models.Model):
    user = models.CharField(max_length=150)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    date = models.DateTimeField()

class Leaderboard(models.Model):
    user = models.CharField(max_length=150)
    score = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
